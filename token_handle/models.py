from django.db import models

# Create your models here.

class tokens(models.Model):
	token = models.CharField(max_length = 2000,default=None)
	expiry = models.CharField(max_length = 1000,default="0")

	def __str__(self):
		return self.token
