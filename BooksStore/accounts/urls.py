from django.urls import path
from accounts.views import profile, register

urlpatterns = [
    path('profile/', profile, name='accounts.profile'),
    path('register/', register, name='accounts.register'),
]