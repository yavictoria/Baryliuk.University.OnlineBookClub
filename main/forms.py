from django.forms import ModelForm
from .models import *
from datetime import date
from django.forms import ModelForm, TextInput, Textarea, Select


class CreateFeedback(ModelForm):
    class Meta:
        model = Feedback
        fields = ["feedback"]
        widgets = {
            'feedback': TextInput(attrs={
                'placeholder': "add your comment",
                'class': "form-control"
            }),
        }


class CreateReport(ModelForm):
    class Meta:
        model = Report
        topics_choices = Topic.objects.order_by('-id')
        fields = ["report", "topic"]
        widgets = {
            'report': TextInput(attrs={
                'placeholder': "add your comment",
                'class': "form-control"
            }),
            'topic': Select(choices=topics_choices, attrs={
                'placeholder': "horror",
                'class': "form-control"
            }),
        }