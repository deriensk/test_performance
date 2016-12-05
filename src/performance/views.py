from django.shortcuts import render, redirect
from .models import Student, Subject
from .forms import StudentModelForm, SubjectModelForm
from django.http import HttpResponseRedirect
# Create your views here.



def student_info(request):
	student_form = StudentModelForm(request.POST or None)
	if student_form.is_valid():
		instance = student_form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'student':student_form,
	}	

	return render(request, 'student.html', context)

def student_subject(request, id=None):
	subject_form = SubjectModelForm(request.POST or None)
	if subject_form.is_valid():
		instance = subject_form.save(commit=False)
		instance.save()
		return redirect('home')
	context = {
		'subject':subject_form,
	}	

	return render(request, 'subject.html', context)

def student_list(request):
	queryset = Subject.objects.all().order_by('-id')
	context = {
		'queryset':queryset,
	}
	return render(request, 'home.html', context)
