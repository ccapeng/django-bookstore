from django.contrib import admin
from .models import \
    Author, Publisher, Category, Book

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book)