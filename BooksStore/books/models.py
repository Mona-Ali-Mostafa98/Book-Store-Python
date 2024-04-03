from django.db import models
from django.shortcuts import  reverse

# Create your models here.
class Book(models.Model):
    image = models.ImageField(upload_to='books/images')
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    pagesNo = models.IntegerField(null=True, blank=True)
    ISBN = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    """ object returned with name"""
    def __str__(self):
        return f'{self.title}'

    @property
    def show_url(self):
        pass
        url = reverse('books.show', args=[self.id])
        return url

    @property
    def delete_url(self):
        pass
        url = reverse('books.delete', args=[self.id])
        return url

    @property
    def image_url(self):
        return f"/media/{self.image}"
