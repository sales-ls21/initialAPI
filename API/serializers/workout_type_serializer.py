from rest_framework import serializers
from API.models import WorkoutType

class WorkoutTypeSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = WorkoutType
		fields = '__all__'