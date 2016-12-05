from rest_framework import serializers, viewsets
from .models import Subject

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Subject
		fields = [
			'student',
			'first_subject',
			'second_subject',
			'third_subject',
				]

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer