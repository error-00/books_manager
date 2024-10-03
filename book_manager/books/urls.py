from django.urls import path
from .views import *

app_name = "books"

urlpatterns = [
    path('books/', BookListCreate.as_view(), name="books-list-create"),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy().as_view(), name="books-retrieve-update-destroy"),
    path('authors/', AuthorListCreate.as_view(), name="authors-list-create"),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy().as_view(), name="authors-retrieve-update-destroy"),
]
