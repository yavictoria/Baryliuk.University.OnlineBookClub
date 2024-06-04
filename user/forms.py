from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, Select, ClearableFileInput, CheckboxInput, BooleanField
from group.models import Interest
from django import forms


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = Profile_user
        interests_choices = Interest.objects.order_by('-id')
        fields = ['description', 'interest', 'images', 'is_author']  # Fields from Profile_user model

        widgets = {
            'description': TextInput(attrs={
                'placeholder': "",
                'class': "form-control"
        }),
            'interest': Select(choices=interests_choices, attrs={
                'placeholder': "",
                'class': "form-control"
        }),
            'images': ClearableFileInput(attrs={
                'placeholder': "select image",
                'static': "images/user_profile.jpg",
                'class': "form-control"
            })
        }

    is_author = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    # Fields from User model
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)

    def __init__(self, *args, **kwargs):
        super(ProfileUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

        # Widgets for User fields
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        user = self.instance.user

        if username and User.objects.exclude(pk=user.pk).filter(username=username).exists():
            self.add_error('username', 'Username already exists.')

        if email and User.objects.exclude(pk=user.pk).filter(email=email).exists():
            self.add_error('email', 'Email already exists.')

        return cleaned_data

    def save(self, commit=True):
        user = self.instance.user
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return super(ProfileUserForm, self).save(commit=commit)

