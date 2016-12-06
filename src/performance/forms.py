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

class SubjectAddForm(forms.Form):
	#subject = forms.CharField()
	subject_name = forms.CharField()
	full_mark = forms.IntegerField()
	pass_mark = forms.IntegerField()
	mark_obtained = forms.IntegerField()

	def clean_subject_name(self):
		subject_name = self.cleaned_data.get("subject_name")
		if len(subject_name) > '':
			return subject_name
		else:
			raise forms.ValidationError("Subject field cannot be blank.")




class SubjectModelForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = [
				'student',
				# 'subject_name',
				# 'full_mark',
				# 'pass_mark',
				# 'mark_obtained',
				]

