from django.contrib import admin
from .models import Student, Subject#, Attendance
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
	model = Subject
	list_display = ['student', 'subject_name', 'full_mark', 'pass_mark', 'mark_obtained']
	list_filter = ['student', 'subject_name']
	list_editable = ['mark_obtained']

    


admin.site.register(Subject, SubjectAdmin)


admin.site.register(Student)
#admin.site.register(Subject)
