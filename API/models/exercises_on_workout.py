from django.db import models
from API.models import Exercises, Workout

class ExercisesOnWorkout(models.Model):

	exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
	workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

	class Meta:
		app_label = "API"
