from django.urls import path
from books.views import (home, index, show, create, edit, delete)

urlpatterns = [
    path('', home, name='books.home'),
    path('index', index, name='books.index'),
    path('create', create, name='books.create'),
    path('<int:id>/show', show, name='books.show'),
    path('<int:id>/edit', edit, name='books.edit'),
    path('<int:id>/delete', delete, name='books.delete')
]

