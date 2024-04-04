from django.db import models
from django.shortcuts import  reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    """ object returned with name"""
    def __str__(self):
        return f'{self.title}'

    @property
    def index_url(self):
        pass
        url = reverse('books.home')
        return url
