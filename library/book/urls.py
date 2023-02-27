from django.urls import path
from . import views

urlpatterns = [

    path('all_books/', views.all_books, name="all_books"),
    path('create_book/', views.create_book, name="create_book"),
    path('view_author/<book_id>', views.view_book, name="view_book"),
    path('search_book/', views.search_book, name="search_book"),
    path('search_user/', views.search_user, name="search_user"),
    ]