from django.db import models
from django.contrib.auth.models import User
from user.models import Profile_user

# Create your models here.

class Session(models.Model):
    topic=models.CharField(max_length=300, blank=False)
    date_start = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    date_end=models.DateTimeField(auto_now_add=False, null=False, blank=False)
    author = models.ForeignKey(Profile_user, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.topic)



class Question(models.Model):
    text = models.TextField(max_length=1000, blank=False)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.text)


class Answer(models.Model):
    question = models.ForeignKey(Question, blank=False, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=False)
