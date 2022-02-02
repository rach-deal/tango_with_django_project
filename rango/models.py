from django.db import models

# Primary Key already provided (id = auto-inc integer field)

class Category(models.Model):
	name = models.CharField(max_length = 128, unique = True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	title = models.CharField(max_length = 128)
	url = models.URLField()
	views = models.IntegerField(default = 0)

	# URL Field same as Char Field, can spec max length
	# DateField stores a Python datetime.date object

	def __str__(self):
		return self.title