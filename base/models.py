from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.email


class Project(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.name, self.user.user.email)


class TaskStatus(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.name, self.project.name[:10])


class Task(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.title[:10], self.project.name[:10])
