# Generated by Django 3.1.7 on 2021-03-21 05:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_of_pub',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 21, 5, 28, 16, 161177, tzinfo=utc), verbose_name='Date/Time'),
        ),
    ]