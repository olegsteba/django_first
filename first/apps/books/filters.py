import django_filters
from django import forms
from .models import Book, Author


class BookFilter(django_filters.FilterSet):

    book_name = django_filters.CharFilter()
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all())

    class Meta:
        model = Book
        exclude = ['image']
        fields = ['book_name', 'author']
