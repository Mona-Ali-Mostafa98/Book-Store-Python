from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, "contacts/index.html", status=200)

