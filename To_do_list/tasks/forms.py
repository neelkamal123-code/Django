from django import forms
from .models import Tasks

class CreateTask(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['date_of_pub']
        labels = {'name_of_task':'Name',
                'task_desc':'Description'}

class EditForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        labels = {'name_of_task':'Task Name','date_of_pub':'Date Published',
        'task_desc':'Description'}
        