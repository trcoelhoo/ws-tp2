from django.http import HttpResponseRedirect
from django.shortcuts import render
from BooksApp.queries import Queries
import mf2py
repo_name = 'books'
port = 7200
endpoint = f'http://localhost:{port}'


def index(request):
    return render(request, 'base.html')


def books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_all_books()
    return render(request, 'books.html', {'books': books})


def home(request):
    q = Queries(endpoint, repo_name)
    nBad = q.get_number_bad_books()
    nGood = q.get_number_good_books()
    nBooks = q.get_number_books()
    nShort = q.get_number_short_books()
    nLong = q.get_number_long_books()
    nPopular = q.get_number_popular_books()
    nSeen = q.get_number_seen_books()

    return render(request, 'index.html',
                  {'nBad': nBad, 'nGood': nGood, 'nBooks': nBooks, 'nShort': nShort, 'nLong': nLong,
                   'nPopular': nPopular, 'nSeen': nSeen})


def book(request, book_isbn):
    q = Queries(endpoint, repo_name)
    book = q.get_book_by_isbn(book_isbn)

    if book['book_image'] is None:
        book['book_image'] = 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'

    status = ""
    if book['has_seen'] == "seen":
        status = "Read"
    else:
        status = "Not Read"
    status="Want to Read"

    #if book['wantRead'] == "true":
    #    status = "Want to Read"

    with open('templates/book.html', 'r') as file:
        obj = mf2py.parse(doc=file)
        print('Book MicroFormats\n\t', obj)

    return render(request, 'book.html', {'book': book, 'status': status})


def update(request, book_isbn):
    q = Queries(endpoint, repo_name)
    q.update_seen(book_isbn)

    # send back to the book page
    url = '/books/' + str(book_isbn) + '/'
    return HttpResponseRedirect(url)


def author(request, author_name):
    q = Queries(endpoint, repo_name)
    author = q.get_author(author_name)
<<<<<<< HEAD
    #image = author['author_image']
    #if image is None:
    #    author['author_image'] = 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'

=======
    image = author['author_image']
    if image is None:
        author['author_image'] = 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'
    print(author['author_image'])
>>>>>>> 3ad1a7b7f2066d92d00827a83a87f824e55a638a
    with open('templates/author.html', 'r') as file:
        obj = mf2py.parse(doc=file)
        print('Author MicroFormats\n\t', obj)
    #author_popularity = q.get_author_popularity(author_name)
    #n_books_written = q.get_n_books_by_author(author_name)
    #return render(request, 'author.html', {'author': author, 'author_name': author_name, 'author_popularity': author_popularity, 'n_books_written': n_books_written})
    return render(request, 'author.html', {'author': author, 'author_name': author_name})


def search_books(request):
    q = Queries(endpoint, repo_name)
    keyword = request.GET.get('searchForm')
    print(f"key: {keyword}")
    title = f"Results for key: {keyword}"
    books = q.search_book(keyword)
    return render(request, 'search.html', {'title': title, "books": books, 'type': 'text'})


def search_books_by_years(request):
    q = Queries(endpoint, repo_name)
    year1 = request.GET.get('year1')
    year2 = request.GET.get('year2')
    print(f"key: {year1} {year2}")
    title = f"Results for years: {year1} to {year2}"
    books = q.search_year(year1, year2)
    return render(request, 'search.html', {'title': title, "books": books, 'type': 'year'})


def good_books(request):
    q = Queries(endpoint, repo_name)
    good_books = q.get_good_books()
    return render(request, 'categories.html', {"title": "Good Books", "books": good_books})


def bad_books(request):
    q = Queries(endpoint, repo_name)
    bad_books = q.get_bad_books()
    return render(request, 'categories.html', {"title": "Bad Books", "books": bad_books})


def popular_books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_popular_books()
    return render(request, 'categories.html', {"title": "Popular Books", "books": books})


def long_books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_long_books()
    return render(request, 'categories.html', {"title": "Long Books", "books": books})


def short_books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_short_books()
    return render(request, 'categories.html', {"title": "Short Books", "books": books})


def seen_books(request):
    q = Queries(endpoint, repo_name)
    read_books = q.get_seen_books()
    #want_read_books = q.get_seen_books())
    # return ender(request, 'userPage.html', {"title": "Read Books", "books": read_books, 'want_read_books': want_read_books})
    return render(request, 'userPage.html', {"title": "Read Books", "books": read_books})
