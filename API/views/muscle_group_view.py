from django.contrib.auth.models import User
from django.shortcuts import render
from API import serializers, models
from rest_framework import viewsets

class BodyPartViewSet(viewsets.ModelViewSet):

	queryset = models.BodyPart.objects.all()
	serializer_class = serializers.BodyPartSerializer

	