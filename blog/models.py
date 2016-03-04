from __future__ import unicode_literals
from django.db import models



# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    review = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    createdDate = models.DateTimeField("2/25/16")