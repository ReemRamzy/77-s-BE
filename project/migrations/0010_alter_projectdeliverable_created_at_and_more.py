# Generated by Django 4.1.7 on 2023-03-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0009_projectproposal_unique_proposal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectdeliverable",
            name="created_at",
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name="projectdeliverable",
            name="modified_at",
            field=models.DateTimeField(editable=False),
        ),
    ]