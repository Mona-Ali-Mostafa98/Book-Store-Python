from django.shortcuts import render, redirect, reverse

# Create your views here.

def profile(request):
    return render(request, "accounts/profile.html", status=200)
