# Generated by Django 3.1.7 on 2021-03-21 08:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20210321_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_of_pub',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 21, 8, 46, 34, 685404, tzinfo=utc), verbose_name='Date/Time'),
        ),
    ]