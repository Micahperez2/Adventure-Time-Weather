from django.db import models

# Create your models here.
class Post(models.Model):
    title_city = models.CharField(max_length=25)
    at_city = models.CharField(max_length=25)
    at_image = models.CharField(max_length=30)
    date = models.CharField(max_length=25)
    temp = models.CharField(max_length=25)
    desc = models.CharField(max_length=25)
