from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse



#created_date = models.DateTimeField(default=timezone.now)

# Create your models here.

ROLL_CHOICE = [tuple([x,x]) for x in range(1,101)]
GRADE_CHOICE = [tuple([x,x]) for x in range(1,11)]
 
class Student(models.Model):
	name = models.CharField(max_length=120)
	grade = models.IntegerField(choices=GRADE_CHOICE)
	roll = models.IntegerField(choices=ROLL_CHOICE)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse("subject_create", kwargs={"id": self.id})	


	def get_absolute_url_2(self):
		return reverse("student_n_sub_detail", kwargs={"id": self.id})	

	
SUBJECT_CHOICES = (
	('', ""),
	('math', "Math"),
	('science', "Science"),
	('geography', "Geography"),
	('spanish', "Spanish"),
	('french', "French"),
	('english', "English"),
	('accounts', "Accounts"),
	)


class Subject(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
	subject_name = models.CharField(max_length=120, choices=SUBJECT_CHOICES, default='')
	full_mark = models.IntegerField(default=100)
	pass_mark = models.IntegerField(default=45)
	mark_obtained = models.IntegerField(blank=True, null=True)
	

	def __str__(self):
		return self.subject_name


	def get_absolute_url_2(self):
		return reverse("student_n_sub_detail", kwargs={"id": self.id})


class Attendance(models.Model):
	pass
		
'''
from django.forms import modelform_factory
from performance.models import Subject
SubjectForm = modelform_factory(Subject, fields=("subject_name", "subject_name", "full_mark", "pass_mark","mark_obtained"))		


'''