from django.conf.urls import url, include

from .views import (
					student_create,
					formset_view,
					modelformset_view,
					subject_create,
					student_n_sub_detail,
					home,
					)

urlpatterns = [
   
   url(r'^$', home, name='home'),
   url(r'^create/$', student_create, name='student_create'),
   url(r'^(?P<id>\d+)/$', subject_create, name='subject_create'),
   url(r'^(?P<id>\d+)/detail$', student_n_sub_detail, name='student_n_sub_detail'),

   url(r'^modelformset/$', modelformset_view, name='modelformset_view'),
   url(r'^formset/$', formset_view, name='formset_view'),
   url(r'^presentation/$', formset_view, name='presentation'),

]
