from django.db import models


class WorkoutType(models.Model):

	name = models.CharField(max_length=20)

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		app_label = "API"