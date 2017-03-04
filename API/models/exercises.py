from django.db import models
from API.models import *

class Exercises(models.Model):

	name = models.CharField(max_length=120)
	description = models.TextField()
	muscle_group = models.ForeignKey(BodyPart, null=True, on_delete=models.CASCADE)
	equipment = models.ForeignKey(Equipment, null=True, on_delete=models.CASCADE)
	url = models.CharField(max_length=300)

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		app_label = "API"