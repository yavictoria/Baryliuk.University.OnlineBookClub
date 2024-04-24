from django.db import models
from group.models import Interest
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    # file will be uploaded to MEDIA_ROOT/images
    images = models.ImageField(upload_to="images/", blank=True, null=True)
    like = models.ManyToManyField(User, blank=True)
    interest = models.ManyToManyField(Interest, blank=True)

    def __str__(self):
        return self.name

