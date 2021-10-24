from django.shortcuts import render
from .forms import AddBookForm


# Create your views here.
def add_book(request):
    context = {}
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            context['request'] = request
            return render(request, "books/addBook.html", context)
    add_book_form = AddBookForm()
    context["form"] = add_book_form
    return render(request, "books/addBook.html", context)
