#django imports
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.shortcuts import render
from django.contrib import messages

# imports from your created files
from categories.models import Category
from categories.forms import CategoryModelForm

def home(request):
    categories = Category.objects.all()
    return render(request, "categories/index.html",
                  context={"categories": categories}, status=200)\

def index(request):
    categories = Category.objects.all()
    return render(request, "categories/crud/index.html",
                  context={"categories": categories}, status=200)


def show(request, id):
    # category = Category.objects.get(id=id)
    category = get_object_or_404(Category, pk=id)
    return render(request, "categories/crud/show.html", context={"category": category})


def delete(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    url = reverse("categories.index")
    messages.success(request, "Category Deleted Successfully.")

    return redirect(url)


def create(request):
    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)

            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            logo = form.cleaned_data['logo']

            category = Category(name=name, description=description, logo=logo)

            category.save()
            messages.success(request, "Category Add Successfully.")
            return redirect(category.show_url)

    return render(request, 'categories/crud/create.html', context={'form': form})


def edit(request, id):
    category = Category.get_category_by_id(id)
    # category = get_object_or_404(Category, pk=id)
    form = CategoryModelForm(instance=category)

    if request.method == "POST":
        form = CategoryModelForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save()

            messages.success(request, "Category updated successfully.")
            return redirect(category.show_url)

    return render(request, 'categories/crud/edit.html', context={"form": form})
