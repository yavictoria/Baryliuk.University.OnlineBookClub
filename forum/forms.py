from django.forms import ModelForm
from .models import *
from datetime import date
from django.forms import ModelForm, TextInput, Textarea, DateInput




class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        today = date.today()
        fields = ["topic", "description"]
        widgets = {
            'topic': TextInput(attrs={
                'placeholder': "add your topic",
                'class': "form-control"
            }),
            'description': Textarea(attrs={
                'placeholder': "add your description",
                'class': "form-control"
            }),
        }


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        today = date.today()
        fields = ["discuss"]
        widgets = {
            'discuss': TextInput(attrs={
                'placeholder': "add your comment",
                'class': "form-control"
            }),
        }