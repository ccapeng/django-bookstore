from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book, Category, Publisher, Author


class BookList(ListView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'category', 'publisher', 'author']
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        ctx = super(BookCreate, self).get_context_data(**kwargs)
        ctx['view'] = "create"
        return ctx


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'category', 'publisher', 'author']
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        ctx = super(BookUpdate, self).get_context_data(**kwargs)
        ctx['view'] = "update"
        return ctx


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


class CategoryList(ListView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        ctx = super(CategoryCreate, self).get_context_data(**kwargs)
        ctx['view'] = "create"
        return ctx


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        ctx = super(CategoryUpdate, self).get_context_data(**kwargs)
        ctx['view'] = "update"
        return ctx


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')


class PublisherList(ListView):
    model = Publisher


class PublisherCreate(CreateView):
    model = Publisher
    fields = ['name']
    success_url = reverse_lazy('publisher_list')

    def get_context_data(self, **kwargs):
        ctx = super(PublisherCreate, self).get_context_data(**kwargs)
        ctx['view'] = "create"
        return ctx


class PublisherUpdate(UpdateView):
    model = Publisher
    fields = ['name']
    success_url = reverse_lazy('publisher_list')

    def get_context_data(self, **kwargs):
        ctx = super(PublisherUpdate, self).get_context_data(**kwargs)
        ctx['view'] = "update"
        return ctx


class PublisherDelete(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher_list')


class AuthorList(ListView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = ['last_name', 'first_name']
    success_url = reverse_lazy('author_list')

    def get_context_data(self, **kwargs):
        ctx = super(AuthorCreate, self).get_context_data(**kwargs)
        ctx['view'] = "create"
        return ctx

    def form_valid(self, form):
        data = self.request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        query = Author.objects.filter(
            first_name=first_name, last_name=last_name)
        authors = query.all()
        if len(authors) > 0:
            form.errors['input invalid'] = 'Author is already exist.'
            return self.form_invalid(form)
        return super(AuthorCreate, self).form_valid(form)


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['last_name', 'first_name']
    success_url = reverse_lazy('author_list')

    def get_context_data(self, **kwargs):
        ctx = super(AuthorUpdate, self).get_context_data(**kwargs)
        ctx['view'] = "update"
        return ctx


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')
