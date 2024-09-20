from django.urls import path
from eduapp.views import home

from . import views

urlpatterns = [
    path('home/', home, name='home'),
    
    # path('save_teachers_data/', views.save_teachers_data, name='save_teachers_data'),  # Form URL
]