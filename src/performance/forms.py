from django import forms
from .models import Student, Subject

class StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
				'name',
				'grade',
				'roll',
				]

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

