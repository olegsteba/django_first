from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Book, PublishingHouse, Author


def get_books_list(requests):
    books = Book.objects.all()
    return render(requests, 'books/index.html', {'title': 'Книги', 'books': books})
