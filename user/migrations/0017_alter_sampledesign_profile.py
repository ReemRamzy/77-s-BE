# Generated by Django 4.2 on 2023-04-16 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0016_alter_clientprofile_timezone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sampledesign",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sample_designs",
                to="user.designerprofile",
            ),
        ),
    ]