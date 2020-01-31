# Generated by Django 3.0.1 on 2020-01-30 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("songbook", "0011_arrangement_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="arrangement",
            name="title",
            field=models.CharField(default="Default Arrangement", max_length=100),
        ),
        migrations.CreateModel(
            name="PersonSchedule",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(default="confirmed", max_length=20)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="songbook.Person",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="songbook.Position",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="plan",
            name="people",
            field=models.ManyToManyField(
                related_name="plans", to="songbook.PersonSchedule"
            ),
        ),
    ]
