from django.contrib import admin
from .models import Student, Subject#, Attendance
# Register your models here.

admin.site.register(Student)
admin.site.register(Subject)
#admin.site.register(Attendance)