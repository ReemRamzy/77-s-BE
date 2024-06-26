# Generated by Django 4.2 on 2023-05-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0021_user_backend"),
    ]

    operations = [
        migrations.AddField(
            model_name="designerprofile",
            name="level",
            field=models.CharField(
                choices=[
                    ("Entry", "Entry"),
                    ("Middle", "Middle"),
                    ("Advanced", "Advanced"),
                ],
                default="Entry",
                max_length=8,
            ),
        ),
    ]
