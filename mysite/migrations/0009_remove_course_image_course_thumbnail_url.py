# Generated by Django 4.0 on 2022-11-26 09:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_remove_course_thumbnail_url_course_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.AddField(
            model_name='course',
            name='thumbnail_url',
            field=models.CharField(default=datetime.datetime(2022, 11, 26, 9, 21, 0, 85164, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
