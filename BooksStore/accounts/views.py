from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from accounts.forms import RegisterForm

# Create your views here.

def profile(request):
    return render(request, "accounts/profile.html", status=200)

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form= RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_url = reverse("login")
            return redirect(login_url)

    return render(request, "accounts/register.html", {"form": form})
