from django.shortcuts import render
from .forms import StudentModelForm
# Create your views here.

def student_info(request):
	student_form = StudentModelForm(request.POST or None)
	if student_form.is_valid():
		instance = student_form.save(commit=False)
		instance.save()
	context = {
		'student':student_form,
	}	

	return render(request, 'student.html', context)