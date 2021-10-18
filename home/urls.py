from django.urls import path
from home.views import home, test_static

urlpatterns = [
    path('', home, name='home'),
    path('test/', test_static)
]
