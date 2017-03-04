from django.db import models
from API.models import AppUser, WorkoutType

class Workout(models.Model):

	name = models.CharField(max_length=50)
	description = models.TextField(max_length=500)
	day = models.CharField(max_length=20)
	goal = models.ForeignKey(WorkoutType, null=True, on_delete=models.CASCADE)
	results = models.TextField(max_length=400, null=True)
	complete = models.IntegerField(default=0)
	user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		app_label = "API"