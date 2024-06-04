from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
    name=models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    topic=models.CharField(max_length=300, blank=False)
    description=models.TextField(max_length=1000, blank=True)
    #link=models.CharField(max_length=100, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.topic)


class Discussion(models.Model):
    forum=models.ForeignKey(Forum, blank=False, on_delete=models.CASCADE)
    name = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    discuss=models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.forum, ", ", self.name)

