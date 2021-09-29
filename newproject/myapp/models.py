from django.db import models

# Create your models here.

class Si(models.Model):
	name = models.CharField(max_length=30)
	principle = models.FloatField()
	time = models.FloatField()
	rate = models.FloatField()
	def __str__(self):
		return self.name

class Employee(models.Model):
	emp_id = models.IntegerField()
	name = models.CharField(max_length=200)
	company = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	salary = models.FloatField()

	def __str__(self):
		return self.name
