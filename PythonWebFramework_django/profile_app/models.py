from django.db import models

# Create your models here.

class InFo(models.Model):
    author: models.CharField(max_length='100') # type:ignore
    details: models.CharField(max_length='600') #type:ignore
    date: models.CharField(max_length='20')   #type:ignore
