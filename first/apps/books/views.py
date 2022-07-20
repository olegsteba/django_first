from django.contrib.sites import requests
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Book, PublishingHouse, Author
from .forms import BookForm
from .filters import BookFilter
from django_filters.views import FilterView


class ListBook(FilterView):
    template_name = 'books/book_list.html'
    queryset = Book.objects.all()
    context_object_name = "books"
    filterset_class = BookFilter


class SearchResultsListView(FilterView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/search_results.html'


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


class BookFormView(FormView):
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = '/book/book_form'

    def form_valid(self, form):
        # book_name = form.cleaned_data['book_name']
        # description = form.cleaned_data['description']
        # authors = [i for i in form.cleaned_data['authors']]
        book = Book(
            book_name=form.cleaned_data['book_name'],
            description=form.cleaned_data['description'],
            author=[i for i in form.cleaned_data['authors']],
        )
        book.save()
        return super(BookFormView, self).form_valid(form)


# def get_books_list(requests):
#     if requests.method == "POST":
#         form = BookForm(requests.POST)
#         if form.is_valid():
#             book_name = form.cleaned_data["book_name"]
#             authors = form.cleaned_data["authors"]
#
#     form = BookForm()
#
#     books = Book.objects.all()
#
#     context = {
#         'title': 'Книги',
#         'books': books,
#         'sale': True,
#         'form': form,
#     }
#     return render(requests, 'books/book_list.html', context)
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

