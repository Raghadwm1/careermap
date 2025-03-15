"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from chat.views import chat_view, room

# for multiple views use round brackets
from personal.views import (
    ExpertBooking,
    StudentHome,
    indexPage,
    home_screen_view, 
    registerStudentPage,
    registerExpertPage,
    loginPage,
    logoutUser,
    redirectExpert,
    room,
)
from django.urls import path

urlpatterns = [
    path('', indexPage, name='index'),
    path("admin/", admin.site.urls),
    path('home/', home_screen_view, name='home'),
    path('registerStudent/', registerStudentPage, name='registerStudent'),
    path('registerExpert/', registerExpertPage, name='registerExpert'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('redirect/', redirectExpert, name='redirectExpert'),
    path('Studenthome/', StudentHome, name='StudentHome'),
    path('ExpertBooking/', ExpertBooking, name='ExpertBooking'),
    path("chat/<str:room_name>/", chat_view, name="chat_room"),
    path("admin/", admin.site.urls),
    path("chat/", include("chat.urls")),  
    path('room/', room, name='room'),

]
