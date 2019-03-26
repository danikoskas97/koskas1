from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=264)
	description = models.TextField()
	image = models.ImageField(default='static/images/type_de_repro/logo_kfbleu.jpg',
	 upload_to='static/images/type_de_repro/')

	def __str__(self):
		return self.name

	def __repr__(self):
  		return "<Product {}>".format(self.name)
