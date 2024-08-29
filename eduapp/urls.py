from django.urls import path
from eduapp.views import home

from . import views

urlpatterns = [
    path('home/', home, name='home'),
]