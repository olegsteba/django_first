from django.shortcuts import HttpResponse
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
        "id_publishing_house__email",
        "id_publishing_house__website_link",
        "id_publishing_house__date_add"
    )
    for book in books:
        print(book)
    return render(requests, 'books/index.html', {'title': 'Книги', 'books': books})
