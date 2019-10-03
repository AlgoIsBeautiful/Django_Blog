from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# create models here

class Category(models.Model):
	'''
		CharField: let the type of input is string
		max_length: total length
		DateTimeField, IntegerField
		more information can check here: https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
	'''
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)


class Post(models.Model):
	'''
	title: article title
	'''
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	# summary can be empty, blank = True means the content can be empty
	abstract = models.CharField(max_length=300, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

# class Post(models.Model):
# 	'''
# 		title: CharField for short title
# 		body: TextField for long contents
# 		create time: DateTimeField()
# 		modified time: DateTimeField()
# 	'''
# 	title = models.CharField('Article', max_length=200)
# 	category = models.ForeignKey('Category', verbose_name='Article Category', on_delete=models.CASCADE)
# 	date_time = models.DateField(auto_now_add=True)
# 	content = models.TextField(blank=True, null=True) # body
# 	digest = models.TextField(blank=True, null=True)
# 	author = models.ForeignKey('ZUOZHESHISHUI', verbose_name='Author', on_delete=models.CASCADE)
# 	view = models.BigIntegerField(default=0) # total number of readers
# 	comment = models.BigIntegerField(default=0) # total number of comment
# 	picture = models.CharField(max_length=200) # picture address
# 	tags = models.ManyToManyField(Tag, blank=True)
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)
#
# 	def __str__(self):
# 		return self.title
#
# 	def viewed(self):
# 		self.view += 1
# 		self.save(update_fields=['view'])
#
# 	def commenced(self):
# 		self.comment += 1
# 		self.save(update_fields=['comment'])
#
# 	class Meta:
# 		ordering = ['-date_time']
#
# class Category(models.Model):
# 	'''
# 		CharField: let the type of input is string
# 		max_length: total length
# 		DateTimeField, IntegerField
# 		more information can check here: https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
# 	'''
# 	name = models.CharField('Category', max_length=100)
# 	created_time = models.DateTimeField()
# 	last_mod_time = models.DateTimeField()
#
# 	class Meta:
# 		ordering = ['name']
# 		verbose_name = 'Articles Category'
# 		verbose_name_plural = verbose_name
#
# 	def __str__(self):
# 		return self.name
#
# class Comment(models.Model):
# 	title = models.CharField('Title', max_length=100)
# 	source_id = models.CharField('id or source name', max_length=25)
# 	create_time = models.DateTimeField('Comment Time:', auto_now=True)
# 	user_name = models.CharField('Username', max_length=25)
# 	url = models.CharField('links', max_length=100)
# 	comment = models.CharField('comments', max_length=1000)