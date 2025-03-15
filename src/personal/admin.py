from django.contrib import admin
from .models import Student
from .models import Expert
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'major', 'level', 'email', 'date_created')

# admin.site.register(Student, StudentAdmin)


# admin.site.register(Student)

# admin.site.unregister(Student)

class StudentInLine(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = "Students"

class ExpertInLine(admin.StackedInline):
    model = Expert
    can_delete = False
    verbose_name_plural = "Experts"

class CustomizedUserAdmin(UserAdmin):
    inlines = (StudentInLine, ExpertInLine)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)

# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'major', 'level') # fields can be adjusted

class ExpertAdmin(admin.ModelAdmin):
    list_display = ('user', 'major', 'jobTitle') # fields can be adjusted
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Expert, ExpertAdmin)