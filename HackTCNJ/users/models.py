from django.db import models
from message.models import School


class AdminUser(models.Model):

    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):

    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





