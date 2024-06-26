#django imports
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

# python imports
import json

# imports from your created files
from books.models import Book
from categories.models import Category
from books.forms import BookModelForm, BookForm

books = [
    {"id":1, "image":"book1.png", "title":"Book #1", "category":"science", "author":"Author Name", "price":"100", "pagesNo":"20", "ISBN":"10"},
    {"id":2, "image":"book2.png", "title":"Book #2", "category":"Programing", "author":"Author Name", "price":"200", "pagesNo":"50", "ISBN":"20"},
    {"id":3, "image":"book3.png", "title":"Book #3", "category":"Network", "author":"Author Name", "price":"300", "pagesNo":"300", "ISBN":"30"},
    {"id":4, "image":"book1.png", "title":"Book #4", "category":"Network", "author":"Author Name", "price":"400", "pagesNo":"100", "ISBN":"40"},
    {"id":5, "image":"book2.png", "title":"Book #5", "category":"science", "author":"Author Name", "price":"500", "pagesNo":"40", "ISBN":"50"},
    {"id":6, "image":"book3.png", "title":"Book #6", "category":"Programing", "author":"Author Name", "price":"600", "pagesNo":"600", "ISBN":"60"},
];

def home(request):
    books = Book.objects.all()
    return render(request, "books/index.html",
                  context={"books": books}, status=200)


def index(request):
    books = Book.objects.all()
    return render(request, "books/crud/index.html",
                  context={"books": books}, status=200)

def show(request, id):
    # book = Book.objects.get(id=id)
    book = get_object_or_404(Book, pk=id)
    return render(request, "books/crud/show.html", context={"book": book})


def delete(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    url = reverse("books.index")
    messages.success(request, "Book Deleted Successfully.")

    return redirect(url)

"""
# delete way by redirect user to delete page
def delete(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        book.delete()
        return redirect('books.index'))

    return render(request,
                    'books/delete.html',
                    {'book': book})"""

"""
# Create before using forms or form model and without validation
def create(request):
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None

        #print(request.POST)

        title = request.POST["title"]
        category = request.POST["category"]
        author = request.POST["author"]
        price = request.POST["price"]
        pagesNo = request.POST["pagesNo"]
        ISBN = request.POST["ISBN"]

        book = Book(
            title=title, category=category, author=author,  price=price, pagesNo=pagesNo, ISBN=ISBN, image=image
        )
        book.save()
        # messages.add_message(request, messages.INFO, "Book Add Successfully")
        messages.success(request, "Book Add Successfully.")

        return redirect(book.show_url)

    # get request
    return  render(request, 'books/crud/create.html')
"""

def create(request):
    form = BookModelForm() # can use BookForm() also
    category = get_object_or_404(Category, pk=1)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)

            title = form.cleaned_data["title"]
            category = category
            author = form.cleaned_data["author"]
            price = form.cleaned_data["price"]
            pagesNo = form.cleaned_data["pagesNo"]
            ISBN = form.cleaned_data["ISBN"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data['image']

            book = Book(title=title, category=category, author=author,  price=price, pagesNo=pagesNo, ISBN=ISBN, description=description, image=image)

            book.save()
            messages.success(request, "Book Add Successfully.")
            return redirect(book.show_url)

    return render(request, 'books/crud/create.html', context={'form': form})


"""
# Edit method before validation and use forms
def edit(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == "POST":
        if "image" in request.FILES:
            image = request.FILES["image"]
            book.image = image

        title = request.POST.get("title")
        category = request.POST.get("category")
        author = request.POST.get("author")
        price = request.POST.get("price")
        pagesNo = request.POST.get("pagesNo")
        ISBN = request.POST.get("ISBN")

        book.title = title
        book.category = category
        book.author = author
        book.price = price
        book.pagesNo = pagesNo
        book.ISBN = ISBN
        book.save()

        messages.success(request, "Book updated successfully.")
        return redirect(book.show_url)

    return render(request, 'books/crud/edit.html', {'book': book})
"""


def edit(request, id):
    book = Book.get_book_by_id(id)
    # book = get_object_or_404(Book, pk=id)
    form = BookModelForm(instance=book)

    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()

            messages.success(request, "Book updated successfully.")
            return redirect(book.show_url)

    return render(request, 'books/crud/edit.html', context={"form": form})


"""
def show(request, id):
    filtered_books = filter(lambda book: book['id'] == id, books)
    filtered_books = list(filtered_books)
    if filtered_books:
        book = filtered_books[0]
        return render(request, "books/show.html", context={
            "book": book
        })

    return HttpResponse("book not found")
"""