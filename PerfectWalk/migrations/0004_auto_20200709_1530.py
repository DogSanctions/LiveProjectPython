# Generated by Django 2.2.5 on 2020-07-09 22:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PerfectWalk', '0003_auto_20200709_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]