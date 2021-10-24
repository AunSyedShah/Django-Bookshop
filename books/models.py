from django.db import models


# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=30, default="blank")
    book_code = models.CharField(max_length=10, default="default0")
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.book_code
