# Generated by Django 4.1.6 on 2023-03-16 21:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0008_designerprofile_rating"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="designerprofile",
            options={"ordering": ["-rating"]},
        ),
    ]
