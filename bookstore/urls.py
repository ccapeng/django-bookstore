"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from book.views import BookList, BookCreate, BookUpdate, BookDelete
from book.views import CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete
from book.views import PublisherList, PublisherCreate, PublisherUpdate, PublisherDelete
from book.views import AuthorList, AuthorCreate, AuthorUpdate, AuthorDelete

#from book.views import books, book_add, book_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookList.as_view(), name='book_list'),
    path('book/', BookList.as_view(), name='book_list'),
    path('book/add/', BookCreate.as_view(), name='book_form'),
    path('book/update/<slug:pk>/', BookUpdate.as_view(), name='book_form'),
    path('book/delete/<slug:pk>/', BookDelete.as_view(),
         name='book_confirm_delete'),

    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/add/', CategoryCreate.as_view(), name='category_form'),
    path('category/update/<slug:pk>/',
         CategoryUpdate.as_view(), name='category_form'),
    path('category/delete/<slug:pk>/', CategoryDelete.as_view(),
         name='category_confirm_delete'),

    path('publisher/', PublisherList.as_view(), name='publisher_list'),
    path('publisher/add/', PublisherCreate.as_view(), name='publisher_form'),
    path('publisher/update/<slug:pk>/',
         PublisherUpdate.as_view(), name='publisher_form'),
    path('publisher/delete/<slug:pk>/', PublisherDelete.as_view(),
         name='publisher_confirm_delete'),

    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/add/', AuthorCreate.as_view(), name='author_form'),
    path('author/update/<slug:pk>/', AuthorUpdate.as_view(), name='author_form'),
    path('author/delete/<slug:pk>/', AuthorDelete.as_view(),
         name='author_confirm_delete'),

]
