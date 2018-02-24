from django.db import models


class School(models.Model):

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Message(models.Model):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    content = models.TextField()
    urgent = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.school)






