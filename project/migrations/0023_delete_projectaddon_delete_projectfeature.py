# Generated by Django 4.2 on 2023-05-30 19:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0022_alter_projectdeliverableattachment_deliverable"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ProjectAddon",
        ),
        migrations.DeleteModel(
            name="ProjectFeature",
        ),
    ]
