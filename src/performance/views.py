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



# def add_info(request):
#     if request.method == "POST":
#         stform = StudentModelForm(request.POST, instance=Student())
#         subforms = [SubjectModelForm(request.POST, prefix=str(x), instance=Subject()) for x in range(0,3)]
#         if stform.is_valid() and all([subf.is_valid() for subf in subforms]):
#             new_stu = stform.save()
#             for cf in subforms:
#                 new_sub = cf.save(commit=False)
#                 new_sub.student = new_stu
#                 new_sub.save()
#             return HttpResponseRedirect('/students/')
#     else:
#         stform = StudentModelForm(instance=Student())
#         subforms = [SubjectModelForm(prefix=str(x), instance=Subject()) for x in range(0,3)]
#     return render(request, 'student.html', {'poll_form': stform, 'choice_forms': subforms})









def student_create(request):
	student_form = StudentModelForm(request.POST or None)
	if student_form.is_valid():
		instance = student_form.save(commit=False)
		instance.save()
		#return redirect('modelformset_view')
		return HttpResponseRedirect(instance.get_absolute_url())
		#modelformset_view
	context = {
		'student':student_form,
	}   

	return render(request, 'student.html', context)


def subject_create(request, id=None):
	instance = get_object_or_404(Student, id=id)
	subject_form = SubjectModelForm(request.POST or None)
	if subject_form.is_valid():
		sub_instance = subject_form.save(commit=False)
		sub_instance.save()
		return HttpResponseRedirect(instance.get_absolute_url_2())
	context = {
		'instance':instance,
		'subject_form':subject_form,
		}
	return render(request, 'subject.html', context)		

def student_n_sub_detail(request, id=None):
	instance_sub = get_object_or_404(Subject, id=id)
	instance_stu = get_object_or_404(Student, id=id)
	context = {
		'instance_sub':instance_sub,
		'instance_stu':instance_stu,
	}
	return render(request, 'stu_n_sub_detail.html', context)





def student_subject(request, id=None):
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






