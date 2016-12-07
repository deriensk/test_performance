from django.shortcuts import render, redirect
from .models import Student, Subject
from .forms import StudentModelForm, SubjectModelForm, SubjectAddForm
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
	# if request.method == 'POST':
	# 	subject_add_form = SubjectAddForm(request.POST or None)

	# 	if subject_add_form.is_valid():
	# 		data = subject_add_form.cleaned_data
	# 		subject_name = data.get('subject_name')
	# 		full_mark = data.get('full_mark')
	# 		pass_mark = data.get('pass_mark')
	# 		mark_obtained = data.get('mark_obtained')
	# 		new_obj = Subject()
	# 		new_obj.subject_name = subject_name
	# 		new_obj.full_mark = full_mark
	# 		new_obj.pass_mark = pass_mark
	# 		new_obj.mark_obtained = mark_obtained
	# 		new_obj.save()
	# 	else:
	# 		subject_add_form = SubjectAddForm()
			
		

	subject_form = SubjectModelForm(request.POST or None)
	if subject_form.is_valid():
		instance = subject_form.save(commit=False)
		instance.save()
		#return redirect('home')
	context = {
		'subject':subject_form,
		#'subject_add_form':subject_add_form,
		
	}	

	return render(request, 'subject.html', context)

def student_list(request):
	queryset = Subject.objects.all().order_by('-id')
	sub = SubjectAddForm
	context = {
		'queryset':queryset,
		'sub':sub,
	}
	return render(request, 'home.html', context)





