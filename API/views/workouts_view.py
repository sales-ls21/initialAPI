from django.contrib.auth.models import User
from django.shortcuts import render
from API import serializers, models
from rest_framework import viewsets

class WorkoutViewSet(viewsets.ModelViewSet):

	queryset = models.Workout.objects.all()
	serializer_class = serializers.WorkoutSerializer

	