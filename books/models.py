from django.db import models
from django.conf import settings
from datetime import datetime


# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=30, default="blank")
    book_code = models.CharField(max_length=10, default="default0")
    quantity_available = models.IntegerField()
    date_posted = models.DateTimeField(default=datetime.now())
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_code
