from django.db import models


class BodyPart(models.Model):

	label = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.label)

	class Meta:
		app_label = "API"