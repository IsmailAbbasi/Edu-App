

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    USER_CHOICES = (
        ('T', 'Teacher'),
        ('S', 'Student'),
    )
    role = models.CharField(max_length=1, choices=USER_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"


class TeachersData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("Date published", auto_now_add=True)
    firstName = models.CharField(max_length=500)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subjects = models.CharField(max_length=100)
    previousexperience = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
