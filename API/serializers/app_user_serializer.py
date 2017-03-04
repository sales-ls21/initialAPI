from rest_framework import serializers
from API.models import AppUser

class AppUserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = AppUser
		fields = '__all__'