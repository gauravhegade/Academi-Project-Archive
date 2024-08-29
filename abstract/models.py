from django.db import models
from django.contrib.auth.models import User


class Mentor(models.Model):
    mid = models.PositiveIntegerField(primary_key=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.mentor.username}"


class Project(models.Model):
    project_id = models.PositiveIntegerField(primary_key=True)
    project_title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.project_id} - {self.project_title}"


class Group(models.Model):
    group_id = models.IntegerField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    mid = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.group_id}"


class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    usn = models.CharField(max_length=10, primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.student.username} - USN:{self.usn}"
