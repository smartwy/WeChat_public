from django.db import models

# Create your models here.

class wcp(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField(default=0)

