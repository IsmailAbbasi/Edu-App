from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import TeachersData  # Import the TeachersData model

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
# @admin.register(TeachersData)
admin.site.register(TeachersData)

class TeachersDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstName', 'lastName', 'city', 'state', 'zipcode', 'experience', 'subjects', 'previousexperience', 'pub_date')
