# Generated by Django 4.2 on 2023-04-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0020_project_is_listed"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectproposal",
            name="accepted",
            field=models.BooleanField(default=False),
        ),
    ]