# Generated by Django 3.1.7 on 2021-03-26 11:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20210326_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_of_pub',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 11, 56, 2, 644425, tzinfo=utc), verbose_name='Date/Time'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='name_of_task',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_desc',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
