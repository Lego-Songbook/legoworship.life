# Generated by Django 3.0.1 on 2020-01-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("songbook", "0005_auto_20200130_1005"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="localization",
            field=models.CharField(default="zh", max_length=50),
        ),
        migrations.AlterField(
            model_name="person",
            name="nick_name",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
