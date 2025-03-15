from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.conf import settings


from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import *
from .forms import CreateStudentUserForm
from .forms import CreateExpertUserForm
from .forms import CreateStudentUserForm


from . import views  # ✅ This imports your app's `views.py`
# from .filters import OrderFilter


@login_required(login_url='login')
def indexPage(request):
    print(request.headers)
    return render(request, "personal/index.html", {})

def home_screen_view(request):
    print(request.headers)
    return render(request, "personal/home.html", {})

# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:

#         form = CreateStudentUserForm()


#         if request.method == 'POST':
#             form = CreateStudentUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)

#                 return redirect('login')

#     context = {'form':form}
#     return render(request, "personal/register.html", context)

def redirectExpert(request):
    # Redirect to the desired page
    return redirect('registerExpert')

def registerStudentPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateStudentUserForm()

        if request.method == 'POST':
            form = CreateStudentUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                major = form.cleaned_data.get('major')
                level = form.cleaned_data.get('level')
                Student.objects.create(user=user, major=major, level=level)  # Create Student instance

                messages.success(request, f'Account was created for {user.username}')
                return redirect('login')

    context = {'form': form}
    return render(request, "personal/registerStudent.html", context)

def registerExpertPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateExpertUserForm()

        if request.method == 'POST':
            form = CreateExpertUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                major = form.cleaned_data.get('major')
                jobTitle = form.cleaned_data.get('jobTitle')
                Student.objects.create(user=user, major=major, jobTitle=jobTitle)  # Create Expert instance

                messages.success(request, f'Account was created for {user.username}')
                return redirect('login')

    context = {'form': form}
    return render(request, "personal/registerExpert.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, "personal/login.html", context)
from django.shortcuts import render

def logoutUser(request):
    logout(request)
    return redirect('login')

def StudentHome(request):
    print(request.headers)
    return render(request, 'personal/StudentHome.html', {})

def ExpertBooking(request):
    print(request.headers)
    return render(request, 'personal/ExpertBooking.html', {})  # Ensure the template exists here

def chat_room(request, room_name):
    return render(request, "chat.html", {"room_name": room_name, "username": request.user.username})

def room(request):
    print(request.headers)
    return render(request, 'chat/room.html', {})
