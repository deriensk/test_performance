from django.conf.urls import url, include

from .views import student_info

urlpatterns = [
   
   url(r'^info/$', student_info, name='student'),
]
