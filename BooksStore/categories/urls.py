from django.urls import path
from categories.views import (home, index, show, create, edit, delete)

urlpatterns = [
    path('', home, name='categories.home'),
    path('index', index, name='categories.index'),
    path('create', create, name='categories.create'),
    path('<int:id>/show', show, name='categories.show'),
    path('<int:id>/edit', edit, name='categories.edit'),
    path('<int:id>/delete', delete, name='categories.delete')
]

