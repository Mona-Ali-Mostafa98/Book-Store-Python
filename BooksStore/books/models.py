from django.db import models
from django.shortcuts import  reverse
from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here.
class Book(models.Model):
    image = models.ImageField(upload_to='books/images')
    title = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(2)])
    category = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])# IntegerField
    pagesNo = models.PositiveIntegerField('Page Numbers', null=True, blank=True)
    ISBN = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
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
