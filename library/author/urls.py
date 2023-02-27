from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('all_authors/', views.all_authors, name="all_authors"),
    path('create_author/', views.create_author, name="create_author"),
    path('delete_author/<author_id>', views.delete_author, name="delete_author"),
    path('author_add_book/<author_id>', views.add_book_to_author, name="add_book"),
    ]