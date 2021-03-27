from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# class User(models.Model):
#     user_name = models.CharField(max_length=20)
#     def __str__(self):a
#         return self.user_name

# class Myuser(models.Model):
#     name = 
class Tasks(models.Model):
    name_of_task = models.CharField(max_length=10)
    task_desc = models.TextField(blank=True,max_length=50) # means desc not neccessary
    date_of_pub = models.DateTimeField("Date/Time",default=timezone.now())
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    # user = models.CharField(max_length=20)
# class Registration(models.Model):
#     name = models.CharField(max_length=20)
#     email = models.EmailField()
#     password = models.