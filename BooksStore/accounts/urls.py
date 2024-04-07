from django.urls import path
from accounts.views import profile

urlpatterns = [
    path('profile/', profile, name='accounts.profile')
]