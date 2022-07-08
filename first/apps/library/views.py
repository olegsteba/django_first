from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Library, User, SeasonTicket


class ListLibrary(ListView):
    template_name = 'library_list.html'
    queryset = Library.objects.all()
    context_object_name = "libraries"


