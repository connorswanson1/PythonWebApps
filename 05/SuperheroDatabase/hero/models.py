from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.ImageField(upload_to='.static/images')
