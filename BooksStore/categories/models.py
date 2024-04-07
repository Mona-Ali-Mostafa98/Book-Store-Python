from django.db import models
from django.core.validators import MinLengthValidator

from django.shortcuts import get_object_or_404, reverse

class Category(models.Model):
    name = models.CharField('Name', max_length=255, unique=True, validators=[MinLengthValidator(2)])
    description = models.TextField('Description', max_length=255, blank=True, null=True)
    logo = models.ImageField('Logo', upload_to='categories/logos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def show_url(self):
        url = reverse("categories.show", args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse("categories.delete", args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('categories.edit', args=[self.id])
        return url

    @property
    def logo_url(self):
        return f"/media/{self.logo}"

    @classmethod
    def get_all_categories(cls):
        categories = cls.objects.all()
        return categories

    @classmethod
    def get_category_by_id(cls, id):
        return get_object_or_404(cls, pk=id)
