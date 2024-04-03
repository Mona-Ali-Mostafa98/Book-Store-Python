from django.shortcuts import render

# Create your views here.
books = [
    {"id":1, "image":"book1.png", "title":"Book #1", "category":"science", "author":"Author Name", "price":"100", "pagesNo":"20", "ISBN":"10"},
    {"id":2, "image":"book2.png", "title":"Book #2", "category":"Programing", "author":"Author Name", "price":"200", "pagesNo":"50", "ISBN":"20"},
    {"id":3, "image":"book3.png", "title":"Book #3", "category":"Network", "author":"Author Name", "price":"300", "pagesNo":"300", "ISBN":"30"},
    {"id":4, "image":"book1.png", "title":"Book #4", "category":"Network", "author":"Author Name", "price":"400", "pagesNo":"100", "ISBN":"40"},
    {"id":5, "image":"book2.png", "title":"Book #5", "category":"science", "author":"Author Name", "price":"500", "pagesNo":"40", "ISBN":"50"},
    {"id":6, "image":"book3.png", "title":"Book #6", "category":"Programing", "author":"Author Name", "price":"600", "pagesNo":"600", "ISBN":"60"},
];


def index(request):
    return render(request, "books/index.html", context = {"books": books}, status=200)


def show(request, id):
    filtered_books = filter(lambda book: book['id'] == id, books)
    filtered_books = list(filtered_books)
    if filtered_books:
        book = filtered_books[0]
        return render(request, "books/show.html", context={
            "book": book
        })

    return HttpResponse("book not found")