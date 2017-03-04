from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):

	first_name = models.CharField(default=None, max_length=60)
	last_name = models.CharField(default=None, max_length=60)
	gender = models.CharField(max_length=50)
	height = models.CharField(max_length=25)
	weight = models.CharField(max_length=5)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	class Meta:
		app_label = "API"