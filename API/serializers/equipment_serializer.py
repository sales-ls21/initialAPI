from rest_framework import serializers
from API.models import Equipment

class EquipmentSerializer(serializers.HyperlinkedModelSerializer):

	model = Equipment
	fields = '__all__'

	