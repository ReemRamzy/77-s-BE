# Generated by Django 4.2 on 2023-04-16 07:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("project", "0021_projectproposal_accepted"),
    ]

    operations = [
        migrations.CreateModel(
            name="FullProjectInvoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reference",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("PAID", "Paid"),
                            ("FAILED", "Failed"),
                        ],
                        default="PENDING",
                        max_length=7,
                    ),
                ),
                ("created_at", models.DateTimeField(editable=False)),
                ("updated_at", models.DateTimeField(editable=False)),
                (
                    "project",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.project",
                    ),
                ),
            ],
            options={
                "ordering": ["-updated_at"],
            },
        ),
    ]
