# Generated by Django 4.1.7 on 2023-03-28 21:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0008_projectdeliverable_image"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="projectproposal",
            constraint=models.UniqueConstraint(
                fields=("project", "designer"), name="unique_proposal"
            ),
        ),
    ]
