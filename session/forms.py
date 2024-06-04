from django.forms import ModelForm
from .models import *
from datetime import date
from django.forms import ModelForm, TextInput, Textarea, DateTimeField


class CreateSession(ModelForm):
    class Meta:
        model = Session

        fields = ["topic", "date_start", "date_end"]
        widgets = {
            'topic' : TextInput(attrs={
            'placeholder' : "It-Stephen King",
            'class' : "form-control"
        }),
            'date_start' : DateTimeField(),
            'date_end' : DateTimeField(),

        }


class CreateQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ["text"]
        widgets = {
            'text': TextInput(attrs={
                'placeholder': "add your question",
                'class': "form-control"
            }),
        }

class CreateAnser(ModelForm):
    class Meta:
        model = Answer
        fields = ["text"]
        widgets = {
            'text': TextInput(attrs={
                'placeholder': "add your answer",
                'class': "form-control"
            }),
        }