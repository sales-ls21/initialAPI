from rest_framework import serializers
from API.models import Exercises

class ExercisesSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Exercises
		fields = '__all__'
