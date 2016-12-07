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


class SubjectAddForm(forms.Form):
	#subject = forms.CharField()
	subject_name = forms.ChoiceField(choices=SUBJECT_CHOICES, required=False)
	full_mark = forms.IntegerField(initial=100)
	pass_mark = forms.IntegerField(initial=45)
	mark_obtained = forms.IntegerField()

	def clean_subject_name(self):
		subject_name = self.cleaned_data.get("subject_name")
		if len(subject_name) == 0:
			return subject_name
		else:
			raise forms.ValidationError("Subject field cannot be blank.")

	
			




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

