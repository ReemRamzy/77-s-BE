# Generated by Django 4.2 on 2023-04-16 05:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0018_alter_project_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="nda",
            new_name="NDA",
        ),
    ]
