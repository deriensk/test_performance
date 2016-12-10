from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Subject
from .forms import StudentModelForm, SubjectModelForm, SubjectAddForm
from django.http import HttpResponseRedirect
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
# Create your views here.

def modelformset_view(request):
	SubjectModelFormset = modelformset_factory(Subject,
				fields=['student', 'subject_name', 'full_mark', 'pass_mark', 'mark_obtained'],
				 extra=3)
	modelformset = SubjectModelFormset(request.POST or None)
	if modelformset.is_valid():
		modelformset.save()
		

	context = {
		'modelformset':modelformset,
	}
	return render(request, 'modelformset_view.html', context)

def formset_view(request):
	SubjectFormset = formset_factory(SubjectAddForm, extra=2)
	formset = SubjectFormset(request.POST or None)
	if formset.is_valid():
		for form in formset:
			print(form.cleaned_data)
	context = {
		'formset':formset,
	}
	return render(request, 'formset_view.html', context)




def student_create(request):
	student_form = StudentModelForm(request.POST or None)
	if student_form.is_valid():
		instance = student_form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
		
	context = {
		'student':student_form,
	}   
	return render(request, 'student.html', context)


def subject_create(request, id=None):
	instance = get_object_or_404(Student, id=id)
	# SubjectModelFormset = modelformset_factory(Subject,
	# 			fields=['subject_name', 'full_mark', 'pass_mark', 'mark_obtained'],
	# 			extra=3)
	# modelformset = SubjectModelFormset(request.POST or None)
	# if modelformset.is_valid():
	# 	modelformset.save()
	subject_form = SubjectModelForm(request.POST or None)
	if subject_form.is_valid():
		sub_instance = subject_form.save(commit=False)
		sub_instance.save()
		return HttpResponseRedirect(instance.get_absolute_url_2())
	context = {
		'instance':instance,
		'subject_form':subject_form,
		#'modelformset':modelformset,

		}
	return render(request, 'subject.html', context)		

def student_n_sub_detail(request, id=None):
	instance_sub = get_object_or_404(Subject, id=id)
	instance_stu = get_object_or_404(Student, id=id)
	#test = get_object_or_404(modelformset_factory(Subject, fields='__all__'))
	context = {
		'instance_sub':instance_sub,
		'instance_stu':instance_stu,
		#'test':test,
	}
	return render(request, 'stu_n_sub_detail.html', context)



def home(request, id=None):
	queryset_student = Student.objects.all()#.order_by('-id')
	
	context = {
		'queryset_student':queryset_student,
		}
	return render(request, 'home.html', context)