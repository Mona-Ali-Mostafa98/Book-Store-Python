from django.shortcuts import render, redirect
from django.shortcuts import  reverse
from django.contrib import messages

# imports from your created files
from contacts.models import Contact

# Create your views here.
# def contact(request):
#     return render(request, "contacts/index.html", status=200)

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        contact = Contact(name=name, email=email, subject=subject,  message=message)
        contact.save()
        messages.success(request, "Your Message Sent Successfully.")

        return redirect(contact.index_url)

    # get request
    return render(request, "contacts/index.html", status=200)
