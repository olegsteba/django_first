from django.urls import path
from .views import ListLibrary

urlpatterns = [
    path('', ListLibrary.as_view(), name="libraries"),
#    path('<int:pk>', BookDetail.as_view(), name="book_info"),
]