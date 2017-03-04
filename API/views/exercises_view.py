from django.contrib.auth.models import User
from django.shortcuts import render
from API import serializers, models
from rest_framework import viewsets

class ExercisesViewSet(viewsets.ModelViewSet):

	queryset = models.Exercises.objects.all()
	serializer_class = serializers.ExercisesSerializer

	