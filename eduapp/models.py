

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
from django.contrib.auth.models import AbstractUser

from django.db import models




class User(AbstractUser):
    USER_CHOICES = (
        ('T', 'Teacher'),
        ('S', 'Student'),
    )
    role = models.CharField(max_length=1, choices=USER_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
