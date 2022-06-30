from django.shortcuts import render
from .models import Book, PublishingHouse, Author


def get_books_list(requests):
    books = Book.objects.all().values(
        "book_name",
        "date_creation",
        "description",
        "id_publishing_house__publishing_house_name",
        "id_publishing_house__address",
        "id_publishing_house__contact_phone",
        "author__first_name",
        "author__last_name",
        "author__country",
    )
    context = {
        'title': 'Книги',
        'books': books,
        'sale': True,
    }
    return render(requests, 'books/index.html', context)
    return render(requests, 'books/index.html', {'title': 'Книги', 'books': books})


