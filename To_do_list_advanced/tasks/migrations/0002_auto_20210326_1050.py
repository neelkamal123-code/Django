# Generated by Django 3.1.7 on 2021-03-26 05:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_of_pub',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 5, 20, 57, 797639, tzinfo=utc), verbose_name='Date/Time'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]