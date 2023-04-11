"""
URL configuration for books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from BooksApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('books/', views.books, name='books'),

    path('books/<str:book_isbn>/', views.book, name='book'),
    path('update/<str:book_isbn>/', views.update, name='update'),
    path('books/authors/<str:author_name>/', views.author, name='author'),

    path('categories/good/', views.good_books, name='good_books'),
    path('categories/bad/', views.bad_books, name="bad_books"),
    path('categories/popular/', views.popular_books, name="popular_books"),
    path('categories/long/', views.long_books, name="long_books"),
    path('categories/short/', views.long_books, name="short_books"),
    path('categories/seen/', views.seen_books, name="seen_books"),
    path('books/search/(?P<keyword>w+)$', views.search_books, name="search_books"),
]
