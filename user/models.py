from django.db import models
from django.contrib.auth.models import User
from group.models import Interest
from django.db.models.fields.files import ImageField


class Profile_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True, null=True)
    interest = models.ForeignKey(Interest, blank=True, on_delete=models.CASCADE, null=True)
    images = models.ImageField(upload_to="images/", blank=True, null=True)
    is_author = models.BooleanField(default=False, blank=True, null=True)