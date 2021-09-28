from django.db import models

# models.Model to interact with the model class Django provides
# in order for us to interact with the database 
class Project(models.Model):

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images/')
	url = models.URLField(blank=True)




