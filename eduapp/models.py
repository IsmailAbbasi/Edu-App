

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
    email = models.CharField(max_length=100, blank=True, null=True)
    contact = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    payment_status = models.BooleanField(default=False)  # or any other field type as required

    # classes = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    # twitter = models.URLField(null=True, blank=True)
    # linkedin = models.URLField(null=True, blank=True)
    CLASS_RANGE_CHOICES = [
        ('1-5', 'Class 1 to 5'),
        ('1-8', 'Class 1 to 8'),
        ('6-10', 'Class 6 to 10'),
        ('6-12', 'Class 6 to 12'),
        ('9-12', 'Class 9 to 12'),
        ('11-12', 'Class 11 to 12'),
    ]
    class_range = models.CharField(max_length=10, choices=CLASS_RANGE_CHOICES, default='1-8')
    # payment_status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='images/', default='images/default-profile-picture1.jpg')

    def get_profile_picture(self):
        return self.photo.url if self.photo else '/static/account/images/default-profile-picture1.jpg'
    def __str__(self):
        return self.username
