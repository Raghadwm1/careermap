from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     username = models.CharField(max_length=200, null=True)
#     first_name = models.CharField(max_length=200, null=True)
#     last_name = models.CharField(max_length=200, null=True)
#     major = models.CharField(max_length=200, null=True)
#     level = models.CharField(max_length=200, null=True)
#     email = models.EmailField()
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    major = models.CharField(max_length=200, null=True)
    level = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    major = models.CharField(max_length=200, null=True)
    jobTitle = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
# # class Order(models.Model):
#     STATUS = ( )