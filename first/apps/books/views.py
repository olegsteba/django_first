from django.shortcuts import render
from .models import Book, PublishingHouse, Author


def get_books_list(requests):
    books = Book.objects.all()
    context = {
        'title': 'Книги',
        'books': books
    }
    return render(requests, 'books/index.html', context)
