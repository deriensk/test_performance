from django.db import models
from django.conf import settings
from django.utils import timezone


#created_date = models.DateTimeField(default=timezone.now)

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=120)
	grade = models.CharField(max_length=120)
	roll = models.IntegerField(default=0)

	def __str__(self):
		return str(self.name)

	

class Subject(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
	first_subject = models.CharField(max_length=120, blank=True, null=True)
	second_subject = models.CharField(max_length=120, blank=True, null=True)
	third_subject = models.CharField(max_length=120, blank=True, null=True)
	

	def __str__(self):
		return str(self.first_subject + self.second_subject + self.third_subject)


# class Attendance(models.Model):
# 	ad_sheet = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)

# 	def __str__(self):
# 		return str(self.ad_sheet)
		