from django.urls import path
from books.views import (home, index, show, create, edit, delete)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home, name='books.home'),
    path('index', login_required(index), name='books.index'),
    path('create', login_required(create), name='books.create'),
    path('<int:id>/show', show, name='books.show'),
    path('<int:id>/edit', login_required(edit), name='books.edit'),
    path('<int:id>/delete', login_required(delete), name='books.delete')
]

