from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class Company(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Jobs(models.Model):
    #Id = models.IntegerField()
	Job = models.CharField(max_length=250)
	category = models.ForeignKey(Category, on_delete = models.CASCADE,null =True, blank = True)
	company = models.ManyToManyField(Company)
	Address = models.TextField(max_length=250)
	views = models.IntegerField(default = 0)
	Deadline = models.DateField(default=timezone.now)
	employmentType = models.CharField(max_length=50, null = True, blank = True)
	URL = models.URLField(
		max_length=128,
		db_index=True,
		unique=False,
		blank=True
	)
	#validThrough = models.CharField(max_length=140)
	#datePosted = models.DateTimeField(default = false,blank=True)
	#keywords = models.ArrayField(max_length=100)

	class Meta:
		ordering = ('-Deadline',)

	def __str__(self):
		return self.Job
		



