# Generated by Django 3.0.3 on 2020-02-07 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0008_add_song_attachment_file_name_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songattachment',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 7, 2, 3, 58, 372615, tzinfo=utc), null=True),
        ),
        migrations.DeleteModel(
            name='Setlist',
        ),
    ]
