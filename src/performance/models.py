from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse



#created_date = models.DateTimeField(default=timezone.now)

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=120)
	grade = models.CharField(max_length=120)
	roll = models.IntegerField(default=0)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse("subject", kwargs={"id": self.id})	

	

class Subject(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
	subject_name = models.CharField(max_length=120, blank=True, null=True)
	full_mark = models.IntegerField(default=100)
	pass_mark = models.IntegerField(default=45)
	mark_obtained = models.IntegerField(blank=True, null=True)
	

	def __str__(self):
		return str(self.subject_name)


class Attendance(models.Model):
	pass
		