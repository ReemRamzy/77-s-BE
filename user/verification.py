from django.conf import settings
from django.core.cache import cache
from django.core.signing import Signer
import jwt
import datetime as dt
from Design77s.logging import logger
from .tasks import send_email_task


class Verification:
    exp = dt.datetime.utcnow() + dt.timedelta(minutes=30)
    signer = Signer(settings.SECRET_KEY)

    @classmethod
    def generate_token(cls, payload: dict, key: str) -> str:
        token = jwt.encode(
            {"exp": cls.exp, **payload}, settings.SECRET_KEY, algorithm="HS256"
        )
        cls.__set_token(key, token)
        return token

    @classmethod
    def __set_token(cls, key: str, token: str):
        cache.set(cls.signer.sign_object(key), token, cls.exp.second)

    @classmethod
    def __get_token(cls, key: str) -> str:
        return cache.get(key)

    @classmethod
    def validate_token(cls, key: str, token: str) -> dict | None:
        key_unsigned = cls.signer.unsign_object(key)
        if cls.__get_token(key) != token:
            print ("Invalid token")
            return None
        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            if decoded_token["email"] == key_unsigned:
                cache.delete(key)
                return decoded_token
            return None
        except jwt.ExpiredSignatureError as e:
            logger.error(e)
            return None

    @classmethod
    def send_email(cls, email: str):
        token = cls.generate_token({"email": email}, key=email)
        print(token)
        url = f"{settings.SITE_URL}/confirm_email?k={cls.signer.sign_object(email)}&t={token}"
        subject, from_email, to = "Email Verification", settings.EMAIL_HOST_USER, email
        send_email_task.delay(to, subject, "email_confirm.html", {"confirm_url": url})
