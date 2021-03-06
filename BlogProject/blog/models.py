from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown


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
	def __str__(self):
		return self.name

class Post(models.Model):
	'''
	title: article title
	'''
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	# summary can be empty, blank = True means the content can be empty
	excerpt = models.CharField(max_length=200, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	views = models.PositiveIntegerField(default=0)

	def save(self, *args, **kwargs):
		if not self.excerpt:
			md = markdown.Markdown(extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
			])
			self.excerpt = strip_tags(md.convert(self.body))[:200]
		super(Post, self).save(*args, **kwargs)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# reverse function, the first parameter is 'blog:detail' name=detail
		return reverse('blog:detail', kwargs={'pk': self.pk})

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	class Meta:
		ordering = ['-created_time']


class Project(models.Model):
    name = models.CharField(max_length=120)
    created_time = models.DateField()
    skills = models.ManyToManyField(Tag)
    intro = models.TextField()
    body = models.TextField()
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
