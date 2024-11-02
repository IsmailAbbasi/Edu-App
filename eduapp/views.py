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

from django.shortcuts import render , redirect
from .models import TeachersData
from .forms import TeachersDataForm
from django.contrib import messages
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def create_profile(request):
    # Check if the logged-in user already has a profile
    if TeachersData.objects.filter(user=request.user).exists():
        messages.error(request, "You already have a profile.")
        return redirect('home')  # Redirect to the home page or profile page

    if request.method == 'POST':
        # Handle profile creation logic
        form = YourProfileForm(request.POST, request.FILES)  # Replace with your actual form
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')  # Redirect after profile creation
    else:
        form = YourProfileForm()

    return render(request, 'create_profile.html', {'form': form})

from .models import TeachersData
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

@login_required



def edit_profile(request, teacher_id):
    teacher = get_object_or_404(TeachersData, id=teacher_id)

    # Ensure only the owner can edit their profile
    if teacher.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this profile.")

    if request.method == 'POST':
        # Update other teacher data fields
        teacher.firstName = request.POST.get('firstName')
        teacher.lastName = request.POST.get('lastName')
        teacher.city = request.POST.get('city')
        teacher.state = request.POST.get('state')
        teacher.experience = request.POST.get('experience')
        teacher.subjects = request.POST.get('subjects')
        teacher.contact = request.POST.get('contact')
        teacher.email = request.POST.get('email')
        teacher.class_range = request.POST.get('class_range')

        # Handle profile picture upload if present
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']
        else:
            # Use the static URL for the default profile picture
            teacher.photo = staticfiles_storage.url('account/images/default-profile-picture1.jpg')

        teacher.save()
        return redirect('home')  # Redirect after saving

    return render(request, 'profile.html', {'teacher': teacher})


@login_required
def profile(request, teacher_id):
    teacher = get_object_or_404(TeachersData, id=teacher_id)
    
    if request.method == 'POST':
        # Update the teacher's data
        teacher.firstName = request.POST['firstName']
        teacher.lastName = request.POST['lastName']
        teacher.city = request.POST['city']
        teacher.state = request.POST['state']
        teacher.experience = request.POST['experience']
        teacher.subjects = request.POST['subjects']
        # teacher.classes = request.POST['classes']
        teacher.contact = request.POST['contact']
        teacher.email = request.POST['email']
        # views.py (inside the form handling view)
        class_range = request.POST.get('class_range')
        teacher.class_range = class_range
        if 'photo' in request.FILES:
            print("here======Izzygnagd")
            teacher.photo = request.FILES['photo']
        
        # Save the teacher data
        teacher.save()
        
        return redirect('home')  # Redirect to home page after saving
    
    return render(request, 'profile.html', {'teacher': teacher})


@login_required
def home(request):
    # Get query parameters (if filtering is needed)
    city_query = request.GET.get('city', '')
    state_query = request.GET.get('state', '')
    subject_query = request.GET.get('subject', '')
    experience_query = request.GET.get('experience', '')

    # Retrieve all teacher profiles from the database
    teachers = TeachersData.objects.all()

    # Apply filters based on the query parameters (if any)
    if city_query:
        teachers = teachers.filter(city__icontains=city_query)
    if state_query:
        teachers = teachers.filter(state__icontains=state_query)
    if subject_query:
        teachers = teachers.filter(subjects__icontains=subject_query)
    if experience_query and experience_query != 'any':
        teachers = teachers.filter(experience=experience_query)

    # Render the home page with all teacher data
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
            teacher_data.user = request.user  
            print(teacher_data)  
            teacher_data.save()
            return redirect('home')  
    else:
        form = TeachersDataForm()
    return render(request, 'teacher.html', {'form': form})
    


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


# razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# def initiate_payment(request, teacher_id):
#     teacher = TeachersData.objects.get(id=teacher_id)
    
#     if teacher.payment_status:
#         return redirect('view_contact_info', teacher_id=teacher.id)

#     # Razorpay order creation
#     payment = razorpay_client.order.create({
#         "amount": 100,  # Amount in paise (INR 100.00)
#         "currency": "INR",
#         "payment_capture": "1"
#     })
    
#     # Pass payment and teacher details to template
#     context = {
#         'payment_id': payment['id'],
#         'razorpay_key': settings.RAZORPAY_KEY_ID,
#         'amount': 100,
#         'teacher': teacher,
#     }
#     return render(request, 'payment.html', context)

# def payment_success(request, teacher_id):
#     teacher = TeachersData.objects.get(id=teacher_id)
#     teacher.payment_status = True
#     teacher.save()
#     return redirect('view_contact_info', teacher_id=teacher_id)


# # views.py
# from django.shortcuts import render

# def view_contact_info(request, teacher_id):
#     teacher = TeachersData.objects.get(id=teacher_id)
#     if not teacher.payment_status:
#         return redirect('home')  # Redirect if payment is not completed
#     return render(request, 'contact_info.html', {'teacher': teacher})


client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

def create_payment(request):
    amount = 500  # Amount in paise 
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'
    notes = {'info': 'Payment for contact details'}

    razorpay_order = client.order.create({
        'amount': amount,
        'currency': order_currency,
        'receipt': order_receipt,
        'notes': notes
    })

    context = {
        'order_id': razorpay_order['id'],
        'amount': amount,
        'razorpay_key': settings.RAZORPAY_API_KEY,
    }
    return render(request, 'payment.html', context)

@csrf_exempt
def verify_payment(request):
    print("yes verifying payment ;) ")
    payment_id = request.GET.get('razorpay_payment_id')
    teacher_id = int(request.GET.get('teacher_id'))
    
    payment = client.payment.fetch(payment_id)
    if payment['status'] == 'authorized' or payment['status'] == 'captured':
        print("yes saving teacher paystatus status ;) ")
        teacher = TeachersData.objects.get(id=teacher_id)
        teacher.payment_status = True
        teacher.save()
        return redirect('view_contact_info', teacher_id=teacher_id)
    else:
        print(payment['status'], payment)
        return redirect('home')
        # return JsonResponse({'status': 'failure'}, status=400)


# def view_profile(request, teacher_id):
#     teacher = get_object_or_404(Teacher, id=teacher_id)
#     show_contact = request.user.has_paid
#     return render(request, 'view_profile.html', {'teacher': teacher, 'show_contact': show_contact})
def view_profile(request, teacher_id):
    teacher = get_object_or_404(TeachersData, id=teacher_id)
    photo_url = teacher.get_profile_picture() 
    return render(request, 'view_profile.html', {'teacher': teacher, 'photo_url': photo_url})

@login_required
def view_contact_info(request, teacher_id):
    teacher = get_object_or_404(TeachersData, id=teacher_id)
    photo_url = teacher.get_profile_picture()
    print(f'Payment Status for {teacher_id}: {teacher.payment_status}')  # Debugging line
    if teacher.payment_status:
        return render(request, 'view_contact_info.html', {
            'teacher': teacher,
            'photo_url': teacher.photo.url if teacher.photo else 'default_image_url.png'  # Use a default if no image
        })
    else:
        return render(request, 'payment.html', {'teacher': teacher, 'photo_url': photo_url})
