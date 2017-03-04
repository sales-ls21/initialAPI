from django.contrib.auth.models import User
from django.shortcuts import render
from API import serializers, models
from rest_framework import viewsets

class ExercisesOnWorkoutViewSet(viewsets.ModelViewSet):

	queryset = models.ExercisesOnWorkout.objects.all()
	serializer_class = serializers.ExercisesOnWorkoutSerializer

	