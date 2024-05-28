# Generated by Django 4.2.4 on 2023-09-01 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0002_alter_chatmessage_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatmessage",
            name="sender",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]