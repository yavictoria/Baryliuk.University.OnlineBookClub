from django.db import models
from django.contrib.auth.models import User



class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False, blank=True, null=True)