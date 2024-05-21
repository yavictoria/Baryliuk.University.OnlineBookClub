from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    feedback = models.TextField(max_length=1000, blank=False)
    user_id = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.feedback)



class Report(models.Model):
    report = models.TextField(max_length=1000, blank=False)
    user_id = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, blank=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.report)

