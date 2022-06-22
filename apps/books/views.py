from django.shortcuts import HttpResponse
from django.shortcuts import render


def get_books_list(requests):
    return HttpResponse('Добро пожаловать в мир книг!')
