from django import forms
from .models import Tasks
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
class CreateTask(forms.ModelForm):
    class Meta:
        model = Tasks
        # fields = '__all__'
        exclude = ['date_of_pub','user']
        labels = {'name_of_task':'Name',
                'task_desc':'Description'}
        # widgets = {'user':forms.HiddenInput()}
# class EditForm(forms.ModelForm):
#     class Meta:
#         model = Tasks
#         fields = 
#         labels = {'name_of_task':'Task Name','date_of_pub':'Date Published',
#         'task_desc':'Description'}
