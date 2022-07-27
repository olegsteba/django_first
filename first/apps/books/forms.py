from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User

from .models import Book, Author


class BookForm(forms.Form):
    author_query = Author.objects.all()
    author_array = (
        [author.id, f"{author.last_name} {author.first_name}"] for author in author_query
    )
    book_name = forms.CharField(min_length=3, label="Название книги")
    description = forms.CharField(label="Описане книги", widget=forms.Textarea)
    authors = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=author_array,
        label="Авторы",
        required=True,
    )

