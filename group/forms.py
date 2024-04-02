from django.forms import ModelForm
from .models import *
from datetime import date
from django.forms import ModelForm, TextInput, Textarea, Select


class CreateGroup(ModelForm):
    class Meta:
        model = Group
        interests_choices = Interest.objects.order_by('-id')

        fields = ["topic", "description", "interest"]
        widgets = {
            'topic' : TextInput(attrs={
            'placeholder' : "It-Stephen King",
            'class' : "form-control"
        }),
            'interest' : Select(choices=interests_choices, attrs={
            'placeholder' : "horror",
            'class' : "form-control"
        }),
            'description': Textarea(attrs={
                'placeholder': "Reading and descussion Stephen King's famous horror novel...",
                'class': "form-control"
        })
        }


class CreateComment(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            'comment': TextInput(attrs={
                'placeholder': "add your comment",
                'class': "form-control"
            }),
        }