from django.db import models



# Create your models here.

class Flower(models.Model):
	title = models.CharField(max_length=255, default='')
	def __str__(self):
		return f"Title: {self.title}"
	description = models.TextField(default='')



