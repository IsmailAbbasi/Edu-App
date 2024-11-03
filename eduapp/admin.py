from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import TeachersData, UserPaymentHistory, UserSubscription  # Import the TeachersData model

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')

class TeachersDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstName', 'lastName', 'city', 'state', 'zipcode', 'experience', 'subjects', 'previousexperience', 'pub_date','email' , 'contact' , 'class_range','photo')
admin.site.register(TeachersData, TeachersDataAdmin)

class UserPaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created_at', 'payment_status')
admin.site.register(UserPaymentHistory, UserPaymentHistoryAdmin)

class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'teacher', 'created_at', 'valid_until')
admin.site.register(UserSubscription, UserSubscriptionAdmin)