from django.conf.urls import url, include

from .views import student_info, student_subject, formset_view, modelformset_view

urlpatterns = [
   
   url(r'^modelformset/$', modelformset_view, name='formset_view'),
   url(r'^formset/$', formset_view, name='formset_view'),
   url(r'^create/$', student_info, name='student'),
   url(r'^(?P<id>\d+)/$', student_subject, name='subject'),
   #url(r'^(?P<id>\d+)/detail$', marks_detail, name='marks_detail'),

]
