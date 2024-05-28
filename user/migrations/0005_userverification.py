# Generated by Django 4.1.6 on 2023-03-14 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_clientprofile_id_card_designerprofile_id_card"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserVerification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_card",
                    models.ImageField(blank=True, null=True, upload_to="id_cards/"),
                ),
                ("accepted", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]