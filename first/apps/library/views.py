from django.shortcuts import HttpResponse
from django.shortcuts import render


def get_library_list(requests):
    return HttpResponse('Добро пожаловать в раздел библиотек!')
