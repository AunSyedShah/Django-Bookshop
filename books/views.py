from django.shortcuts import render


# Create your views here.
def add_book(request):
    return render(request, "books/addBook.html")
