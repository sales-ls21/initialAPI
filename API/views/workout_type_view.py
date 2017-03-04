from django.contrib.auth.models import User
from django.shortcuts import render
from API import serializers, models
from rest_framework import viewsets

class WorkoutTypeViewSet(viewsets.ModelViewSet):

	queryset = models.WorkoutType.objects.all()
	serializer_class = serializers.WorkoutTypeSerializer

	