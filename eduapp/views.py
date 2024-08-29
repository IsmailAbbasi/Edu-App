from django.shortcuts import render,redirect
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User  # Import User model
from allauth.account.forms import LoginForm
from allauth.account.views import SignupView
from django.urls import reverse
from django.db import models

from django.contrib.auth.decorators import login_required
from .models import User


@login_required
def student(request):
    return render(request, 'student.html')

@login_required
def teacher(request):
    return render(request, 'teacher.html')

class CustomSignupView(SignupView):
    def get_success_url(self):
        # Redirect to the role selection page after signup
        return reverse('role')

# def register(request):
#     form = SignupForm()
#     return render(request, 'register.html', {'form': form})

# def login(request):
#     form = LoginForm()
#     return render(request, 'login.html', {'form': form})
# def signup(request):
#     form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

@login_required
def role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        # user.created = User.objects.get_or_create(user=request.user)
        request.user.role = 'T' if role == 'teacher' else 'S'
        request.user.save()

        if role == 'student':
            return redirect('student_page')  # Redirect to the student page
        elif role == 'teacher':
            return redirect('teacher_page')  # Redirect to the teacher page
        else:
            return redirect('home')  # Redirect to home if no role is selected
    return render(request, 'role.html')


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request, 'dashboard.html')

class ChangeUsername(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username']
    template_name = 'change_username.html'
    success_message = "Username updated successfully"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('account_login')

