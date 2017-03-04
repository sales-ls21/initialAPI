from rest_framework import serializers
from API.models import ExercisesOnWorkout

class ExercisesOnWorkoutSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = ExercisesOnWorkout
		fields = '__all__'