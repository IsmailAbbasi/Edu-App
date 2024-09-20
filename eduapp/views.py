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
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import TeachersData
from .forms import TeachersDataForm

# @login_required
# def home(request):
#     if request.user.is_authenticated:  # Check if the user is authenticated

#         teachers = TeachersData.objects.all()
#     else:
#         teachers = None    
#     # print(teachers) 
#     return render(request, 'home.html', {'teachers': teachers})

from django.shortcuts import render
from django.db.models import Q  # For advanced querying
from .models import TeachersData
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # Fetch all teachers initially
    teachers = TeachersData.objects.all()

    # Get the search and filter parameters from the request (default to None if not provided)
    name = request.GET.get('name', None)
    location = request.GET.get('location', None)
    subject = request.GET.get('subject', None)
    experience_min = request.GET.get('experience_min', None)
    experience_max = request.GET.get('experience_max', None)

    # Apply filters based on search parameters if they are provided
    if name:
        teachers = teachers.filter(Q(firstName__icontains=name) | Q(lastName__icontains=name))

    if location:
        teachers = teachers.filter(Q(city__icontains=location) | Q(state__icontains=location) | Q(zipcode__icontains=location))

    if subject:
        teachers = teachers.filter(subjects__icontains=subject)

    if experience_min:
        teachers = teachers.filter(experience__gte=experience_min)
    if experience_max:
        teachers = teachers.filter(experience__lte=experience_max)

    # Render the home page with filtered or unfiltered teachers data
    return render(request, 'home.html', {'teachers': teachers})


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


# def home(request):
#     return render(request, 'home.html')

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


from django.shortcuts import render, redirect
from .forms import TeachersDataForm

def save_teachers_data(request):
    if request.method == "POST":
        form = TeachersDataForm(request.POST)
        if form.is_valid():
            teacher_data = form.save(commit=False)
            teacher_data.user = request.user  # Ensure the user is set correctly
            print(teacher_data)  
            teacher_data.save()
            return redirect('home')  # Redirect after saving
    else:
        form = TeachersDataForm()
    return render(request, 'teacher.html', {'form': form})
    

# from django.shortcuts import render, redirect
# from allauth.account.forms import LoginForm, SignupForm
# from allauth.account.views import SignupView  # Import SignupView from allauth
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.urls import reverse_lazy, reverse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User  # Import User model
# from .models import TeachersData
# from .forms import TeachersDataForm
# from django.views.generic import UpdateView



# def home(request):
#     teachers = TeachersData.objects.all()
#     return render(request, 'home.html', {'teachers': teachers})

# @login_required
# def student(request):
#     return render(request, 'student.html')

# @login_required
# def teacher(request):
#     return render(request, 'teacher.html')

# class CustomSignupView(SignupView):
#     def get_success_url(self):
#         # Redirect to the role selection page after signup
#         return reverse('role')

# @login_required
# def role(request):
#     if request.method == 'POST':
#         role = request.POST.get('role')
#         request.user.role = 'T' if role == 'teacher' else 'S'
#         request.user.save()

#         if role == 'student':
#             return redirect('student_page')
#         elif role == 'teacher':
#             return redirect('teacher_page')
#         else:
#             return redirect('home')
#     return render(request, 'role.html')

# def contact(request):
#     return render(request, 'contact.html')

# def dashboard(request):
#     return render(request, 'dashboard.html')

# class ChangeUsername(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = User
#     fields = ['username']
#     template_name = 'change_username.html'
#     success_message = "Username updated successfully"

#     def get_object(self, queryset=None):
#         return self.request.user

#     def get_success_url(self):
#         return reverse_lazy('account_login')

# def save_teachers_data(request):
#     if request.method == "POST":
#         form = TeachersDataForm(request.POST)
#         if form.is_valid():
#             teacher_data = form.save(commit=False)
#             teacher_data.user = request.user
#             teacher_data.save()
#             return redirect('home')
#     else:
#         form = TeachersDataForm()
#     return render(request, 'teacher.html', {'form': form})
