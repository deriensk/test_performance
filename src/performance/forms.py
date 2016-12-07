from django import forms
from .models import Student, Subject

from django.forms import modelform_factory

class StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
				'name',
				'grade',
				'roll',
				]

SUBJECT_CHOICES = [
	('', ""),
	('math', 'Math'),
	('science', 'Science'),
	('geography', 'Geography'),
	('spanish', 'Spanish'),
	('french', 'French'),
	('english', 'English'),
	('accounts', 'Accounts'),
	]





class SubjectAddForm(forms.Form):
	#name = forms.ModelChoiceField(queryset = Student.objects.all())
	subject_name = forms.CharField(label='Subject',
						widget=forms.Select(choices=SUBJECT_CHOICES))
	full_mark = forms.IntegerField(initial=100)
	pass_mark = forms.IntegerField(initial=45)
	mark_obtained = forms.IntegerField()




class SubjectModelForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = [
				'student',
				'subject_name',
				'full_mark',
				'pass_mark',
				'mark_obtained',
				]
		#exclude = ['student']

