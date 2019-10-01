from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	'''
		CharField: let the type of input is string
		max_length: total length
		DateTimeField, IntegerField
		more information can check here: https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
	'''
	name = models.CharField(max_length=100)

class Tag(models.Model):
	name = models.CharField(max_length=100)

class Post(models.Model):
	'''
		title: CharField for short title 
		body: TextField for long contents
		create time: DateTimeField()
		modified time: DateTimeField()

	
	
	
	'''
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	
	excerpt = models.CharField(max_length=200, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

