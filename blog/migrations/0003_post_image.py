# Generated by Django 4.0 on 2022-11-26 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201004_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Newspic/', verbose_name='Maqola rasmi'),
            preserve_default=False,
        ),
    ]
