from django.db import models

# Create your models here.

class MySimpleModel(models.Model):
	col= models.CharField(max_length=10)