"""
URL configuration for education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from eduapp.views import  home, contact, dashboard, ChangeUsername, role , CustomSignupView , student, teacher
from django.shortcuts import redirect


urlpatterns = [
    path("eduapp/", include("eduapp.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('signup/', signup, name='signup'),
    # path('login/', login, name='login'),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/change-username/', ChangeUsername.as_view(), name='account_change_username'),
    path('role/', role, name='role'),
    path('student/', student, name='student_page'),  # Add name for the student page
    path('teacher/', teacher, name='teacher_page'),
    path('signup/', CustomSignupView.as_view(), name='account_signup'),


]


