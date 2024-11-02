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
from eduapp.views import  home, contact, dashboard, ChangeUsername, role , CustomSignupView , student, teacher , save_teachers_data , profile, view_profile, edit_profile, verify_payment,view_contact_info 
from django.shortcuts import redirect
from eduapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("eduapp/", include("eduapp.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/change-username/', ChangeUsername.as_view(), name='account_change_username'),
    path('role/', role, name='role'),
    path('student/', student, name='student_page'),  # Add name for the student page
    path('teacher/', teacher, name='teacher_page'),
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('save_teachers_data/', save_teachers_data, name='save_teachers_data'),
    path('profile/<int:teacher_id>/', profile, name='profile'),

    # Edit profile URL (this allows editing a teacher's profile)
    path('profile/<int:teacher_id>/edit/', edit_profile, name='edit_profile'),
    path('profile/view/<int:teacher_id>/', view_profile, name='view_profile'),
    path('verify_payment/', verify_payment, name='verify_payment'),
    path('view_contact_info/<int:teacher_id>/', view_contact_info, name='view_contact_info')


] 
    # path('initiate_payment/<int:teacher_id>/', views.initiate_payment, name='initiate_payment'),
    # path('payment_success/<int:teacher_id>/', views.payment_success, name='payment_success'),
    # path('contact_info/<int:teacher_id>/', views.view_contact_info, name='view_contact_info'),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
