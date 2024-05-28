# Generated by Django 4.2 on 2023-04-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_sitesettings"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="behance_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="facebook_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="instagram_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="twitter_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
