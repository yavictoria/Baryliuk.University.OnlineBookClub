from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Interest(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Group(models.Model):
    topic=models.CharField(max_length=300, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    interest=models.ForeignKey(Interest, blank=True, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.topic)


class RelGroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'user')
        #ordering = ['-actor']


class Comment(models.Model):
    comment = models.TextField(max_length=1000, blank=False)
    user_id = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, blank=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    parent_comment = models.ForeignKey('self', blank=True, null=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.comment)
