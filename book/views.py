from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book, Category, Publisher, Author


class BookList(ListView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'category', 'publisher', 'author']
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'category', 'publisher', 'author']
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    

class CategoryList(ListView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('category_list')


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('category_list')


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')


class PublisherList(ListView):
    model = Publisher


class PublisherCreate(CreateView):
    model = Publisher
    fields = ['name']
    success_url = reverse_lazy('publisher_list')


class PublisherUpdate(UpdateView):
    model = Publisher
    fields = ['name']
    success_url = reverse_lazy('publisher_list')


class PublisherDelete(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher_list')


class AuthorList(ListView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = ['last_name', 'first_name']
    success_url = reverse_lazy('author_list')


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['last_name', 'first_name']
    success_url = reverse_lazy('author_list')


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')