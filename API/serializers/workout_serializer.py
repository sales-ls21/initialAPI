from rest_framework import serializers
from API.models import Workout

class WorkoutSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Workout
		fields = '__all__'