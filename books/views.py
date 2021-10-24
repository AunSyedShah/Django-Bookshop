from django.shortcuts import render
from .forms import AddBookForm


# Create your views here.
def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "books/addBook.html")
    add_book_form = AddBookForm()
    context = {
        'form': add_book_form
    }
    return render(request, "books/addBook.html", context)
