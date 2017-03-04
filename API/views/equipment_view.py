from django.contrib.auth.models import User
from django.shortcuts import render
from API import serializers, models
from rest_framework import viewsets

class EquipmentViewSet(viewsets.ModelViewSet):

	queryset = models.Equipment.objects.all()
	serializer_class = serializers.EquipmentSerializer

	