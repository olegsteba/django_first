from django.urls import path
from .views import ListBook, BookDetail, BookFormView

urlpatterns = [
    path('', ListBook.as_view(), name="books"),
    path('<int:pk>', BookDetail.as_view(), name="book_info"),
    path('book_form', BookFormView.as_view(), name="book_form"),
]

