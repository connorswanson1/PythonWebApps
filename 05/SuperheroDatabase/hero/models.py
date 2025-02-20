from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}. {self.name}'
