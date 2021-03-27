from django.db import models
from django.utils import timezone
# Create your models here.
class Tasks(models.Model):
    name_of_task = models.CharField(max_length=50)
    task_desc = models.TextField(blank=True) # means desc not neccessary
    date_of_pub = models.DateTimeField("Date/Time",default=timezone.now())