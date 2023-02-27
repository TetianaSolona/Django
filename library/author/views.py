from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Author
from book.models import Book
from .forms import AuthorFrom


def home(request):
    return render(request, 'author/home.html', {})


def create_author(request):
    if request.method == 'POST':
        form = AuthorFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_authors')
    else:
        form = AuthorFrom
        return render(request, 'author/create_author.html', {'form': form})


def all_authors(request):
    authors = Author.get_all()
    context = {
        'authors': authors
        }
    return render (request, "author/all_authors.html", context=context)


def delete_author(request, author_id):
    if Author.objects.filter(books__isnull=False, id=author_id):
        messages.success(request, f"Author has book, you can`t delete")
    else:
        Author.delete_by_id(author_id)
    return redirect('all_authors')


def add_book_to_author(request, author_id):
    books = Book.get_all()
    author = Author.get_by_id(author_id)
    
    if request.method == 'POST':
        chosen_book = request.POST['book']
        author = Author.get_by_id(author_id)
        if author:
            author.books.add(chosen_book)
            author.save()
            messages.success(request, f"You have Added Author: {author} to Book Id: {chosen_book}")
            return redirect('all_authors')
        else:
            messages.success(request, "Something went wrong")
            return redirect('all_authors')
    else:
        
        context = {
        "books": books,
        "author": author
        }
        return render(request, 'author/author_add_book.html', context=context)
