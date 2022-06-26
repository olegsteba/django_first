from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Book


def get_books_list(requests):
    book = Book.objects.get(id_publishing_house__publishing_house_name="Дрофа")
    print(book.book_name)
    return HttpResponse(f"<h1>{book.book_name}</h1>")
