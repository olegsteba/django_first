from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Book, PublishingHouse, Author


class ListBook(ListView):

    template_name = 'book_list.html'
    queryset = Book.objects.all()
    context_object_name = "books"


class BookDetail(DetailView):
    #template_name = 'book_detail.html'
    # queryset = Book.objects.get(pk=id_book)
    model = Book
    pk_url_kwarg = 'pk'
    # def get_object(self, id_book):
    #     book = Book.objects.get(pk=id_book)
    #     return book

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {
    #        'title': 'Книги',
    #        'books': self.queryset,
    #        'sale': True,
    #     }
    #
    #     return context

# def get_books_list(requests):
#     books = Book.objects.all()
#     context = {
#         'title': 'Книги',
#         'books': books,
#         'sale': True,
#     }
#     for book in books:
#         print(book.author)
#     return render(requests, 'books/index.html', context)
#
#
# def get_book_info(requests, id_book):
#     books = Book.objects.get(pk=id_book)
#     context = {
#         'title': 'Книги',
#         'books': books,
#         'sale': True,
#     }
#     return render(requests, 'books/index.html', context)

