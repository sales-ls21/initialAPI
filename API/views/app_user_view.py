from django.contrib.auth.models import User
from django.shortcuts import render
from API import serializers, models
from rest_framework import viewsets

class AppUserViewSet(viewsets.ModelViewSet):

	queryset = models.AppUser.objects.all()
	serializer_class = serializers.AppUserSerializer

