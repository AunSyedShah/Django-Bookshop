from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home\index.html', context={"title": "Home - Bookshop"})


def test_static(request):
    return render(request, 'home\js_test.html')
