from django.shortcuts import render
from .forms import BookForm
from django.http import HttpResponse


# Create your views here.
def create_book(request):
    form = BookForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form_data = BookForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse("<p>Form Submitted Successfully</p>")
    else:
        return render(request, "book.html", context)
