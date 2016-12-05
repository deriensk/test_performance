from django.conf.urls import url, include

from .views import student_info, student_subject, student_list

urlpatterns = [
   
   url(r'^$', student_list, name='home'),
   url(r'^info/$', student_info, name='student'),
   url(r'^info/(?P<id>\d+)/$', student_subject, name='subject'),

]
