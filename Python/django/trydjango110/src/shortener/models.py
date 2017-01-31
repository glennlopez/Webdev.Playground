from django.db import models

# Create your models here.
class KirrURL(models.Model):
	url 			= models.CharField(max_length=220,)
	shortcode 		= models.CharField(max_length=15, unique=True)
	#shortcode 		= models.CharField(max_length=15, null=False, blank=False)
	#shortcode 		= models.CharField(max_length=15, null=True)
	#shortcode 		= models.CharField(max_length=15, default='cfedefaultshortcode')
	updated 		= models.DateTimeField(auto_now=True) #every save
	timestamp 		= models.DateTimeField(auto_now_add=True) #when created
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		#return str(self.id)
		return str(self.url)



'''
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''
