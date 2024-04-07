from django.db import models
from django.shortcuts import reverse, get_object_or_404
from django.core.validators import MinValueValidator, MinLengthValidator
from categories.models import Category

# Create your models here.
class Book(models.Model):
    image = models.ImageField(upload_to='books/images')
    title = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(2)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="allBooks")
    author = models.CharField(max_length=100, null=True, blank=True)
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
        url = reverse('books.delete', args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('books.edit', args=[self.id])
        return url

    @property
    def image_url(self):
        return f"/media/{self.image}"

    @classmethod
    def get_book_by_id(cls, id):
        return get_object_or_404(cls, pk=id)
