from django.db import models

# Create your models here.

class Token(models.Model):
	username = models.CharField(max_length=100)
	token = models.CharField(max_length=300)

	def __str__(self):
		return self.username

class Profile(models.Model):
	username = models.CharField(max_length=100, unique=True)

	name = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	avatar = models.CharField(max_length=100)


	def __str__(self):
		return self.username