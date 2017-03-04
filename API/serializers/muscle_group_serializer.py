from rest_framework import serializers
from API.models import BodyPart

class BodyPartSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = BodyPart
		fields = '__all__'