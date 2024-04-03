from django.urls import path
from abouts.views import (about)

urlpatterns = [
    path('about', about, name='abouts.index'),
]
