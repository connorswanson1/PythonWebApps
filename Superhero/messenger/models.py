from django.db import models
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User


class Message(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('message_detail', args=[str(self.id)])


