# Generated by Django 4.2.4 on 2023-08-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_dispute_clarification_alter_dispute_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dispute",
            name="clarification",
            field=models.TextField(blank=True, null=True),
        ),
    ]
