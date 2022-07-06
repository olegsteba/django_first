from django.urls import path
from .views import ListBook, BookDetail

urlpatterns = [
    path('', ListBook.as_view(), name="books"),
    path('<int:pk>', BookDetail.as_view(), name="book_info"),
]

