from django.conf.urls import url, include

from .views import student_info, student_subject, student_list#, marks_detail

urlpatterns = [
   
   url(r'^$', student_list, name='home'),
   url(r'^create/$', student_info, name='student'),
   url(r'^(?P<id>\d+)/$', student_subject, name='subject'),
   #url(r'^(?P<id>\d+)/detail$', marks_detail, name='marks_detail'),

]
