# Generated by Django 4.2.4 on 2023-09-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contest", "0002_alter_contest_round_two_finalists"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contest",
            name="released",
            field=models.BooleanField(
                default=False, help_text="Release the reward to the the winner"
            ),
        ),
    ]
