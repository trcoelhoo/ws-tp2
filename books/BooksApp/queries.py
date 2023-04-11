from .GraphDB import GraphDB


class Queries:
    # Get the number of short books (less than 1000 pages)
    nShortBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "short" .
    }
    """

    # Get short books
    shortBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_genre "short" .
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
    }
    """

    # Get the number of books with a rating of 4.5 or higher
    nGoodBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "good" .
    }
    """

    # Get good books
    goodBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_genre "good" .
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
    }
    """

    # Get the number of books with a rating lower than 4.5
    nBadBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "bad" .
    }
    """

    # Get bad books
    badBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_genre "bad" .
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
    }
    """

    # Get the number of books long books (more than 1000 pages)
    nLongBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "long" .
    }
    """

    # Get long books
    longBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_genre "long" .
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
    }
    """

    # Get the number of popular books (more than 10000 ratings)
    nPopularBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "popular" .
    }
    """

    # Get popular books
    popularBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_genre "popular" .
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
    }
    """

    # Get the number of books
    nBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre ?genre .
    }
    """

    # Get the number of books seen
    nSeenBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_seen "true"^^xsd:boolean .
    }
    """

    # Get seen books
    seenBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_seen "true"^^xsd:boolean .
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
    }
    """

    # Get all books
    allBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
    }
    """

    # Search for a book by title, author, isbn or publisher
    searchBook = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    PREFIX authors: <http://books.com/authors/>
    PREFIX publishers: <http://books.com/publishers/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
        FILTER regex(?title, "toSearch", "i")
        }
        UNION
        {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
        FILTER regex(?isbn, "toSearch", "i")
        }
        UNION
        {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
        FILTER regex(?author_name, "toSearch", "i")
        }
        UNION
        {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
        FILTER regex(?publisher_name, "toSearch", "i")
        }
    }
    """

    # Search by year
    searchYear = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
        FILTER (?publication_date > "year1-01-01"^^xsd:date && ?publication_date < "year2-01-01"^^xsd:date)
    }
    """

    # Get book by isbn
    getBook = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
        FILTER regex(?isbn, "replace", "i")
    }
    """

    # Updates the book to the inverse of the current value
    updateBook = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    DELETE {
        ?book pred:has_seen ?has_seen .
    }
    INSERT {
        ?book pred:has_seen ?new_has_seen .
    }
    WHERE {
        ?book pred:has_isbn ?isbn .
        ?book pred:has_seen ?has_seen .
        BIND (IF(?has_seen = "true"^^xsd:boolean, "false"^^xsd:boolean, "true"^^xsd:boolean) AS ?new_has_seen)
        FILTER regex(?isbn, "replace", "i")
    }
    """

    # Get books from author
    getBooksByAuthor = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_genre ?genre .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
        FILTER regex(?author_name, "replace", "i")
    }
    """

    def __init__(self, endpoint, repo_name):
        self.endpoint = endpoint
        self.repo_name = repo_name
        self.db = GraphDB(endpoint, repo_name)

    def get_number_short_books(self):
        response = self.db.query(self.nShortBooks)
        return response[0]['count']['value']

    def get_short_books(self):
        return self.get_books(self.shortBooks)

    def get_number_good_books(self):
        response = self.db.query(self.nGoodBooks)
        return response[0]['count']['value']

    def get_good_books(self):
        return self.get_books(self.goodBooks)

    def get_number_bad_books(self):
        response = self.db.query(self.nBadBooks)
        return response[0]['count']['value']

    def get_bad_books(self):
        return self.get_books(self.badBooks)

    def get_number_long_books(self):
        response = self.db.query(self.nLongBooks)
        return response[0]['count']['value']

    def get_long_books(self):
        return self.get_books(self.longBooks)

    def get_number_popular_books(self):
        response = self.db.query(self.nPopularBooks)
        return response[0]['count']['value']

    def get_popular_books(self):
        return self.get_books(self.popularBooks)

    def get_number_books(self):
        response = self.db.query(self.nBooks)
        return response[0]['count']['value']

    def get_all_books(self):
        return self.get_books(self.allBooks)

    def get_number_seen_books(self):
        response = self.db.query(self.nSeenBooks)
        return response[0]['count']['value']

    def get_seen_books(self):
        query = self.seenBooks
        return self.get_books(query)

    def get_books(self, query):
        response = self.db.query(query)
        books = dict()
        for elem in response:
            isbn = elem['isbn']['value']
            # check if the book is already in the list and if it is, add the author to the list of
            # authors and the genre to the list of genres if it is not already there
            if isbn in books:
                author = elem['author_name']['value']
                genre = elem['genre']['value']

                # check if the author is already in the list of authors
                if author not in books[isbn]['author_name']:
                    books[isbn]['author_name'].append(author)

                # check if the genre is already in the list of genres
                if genre not in books[isbn]['genre']:
                    books[isbn]['genre'].append(genre)

            else:
                book_info = dict()
                book_info['isbn'] = isbn
                book_info['title'] = elem['title']['value']
                book_info['pages'] = elem['pages']['value']
                book_info['rating'] = elem['rating']['value']
                book_info['reviews'] = elem['reviews']['value']
                book_info['has_seen'] = elem['has_seen']['value']
                book_info['publisher_name'] = elem['publisher_name']['value']

                book_info['genre'] = [elem['genre']['value']]
                book_info['author_name'] = [elem['author_name']['value']]
                book_info['language'] = self.__get_language(elem['language']['value'])
                book_info['publication_date'] = elem['publication_date']['value'].split('T')[0]

                books[isbn] = book_info

        books = [books[isbn] for isbn in books]
        return books

    def __get_language(self, language):
        if language == 'eng':
            return 'English'
        elif language == 'spa':
            return 'Spanish'
        elif language == 'fre':
            return 'French'
        elif language == 'ger':
            return 'German'
        elif language == 'ita':
            return 'Italian'
        elif language == 'por':
            return 'Portuguese'
        elif language == 'tur':
            return 'Turkish'
        elif language == 'jpn':
            return 'Japanese'
        elif language == 'rus':
            return 'Russian'
        elif language == 'chi':
            return 'Chinese'
        else:
            return language

    def search_book(self, keyword):
        query = self.searchBook.replace("toSearch", keyword)
        return self.get_books(query)

    def search_year(self, year1, year2):
        query = self.searchYear.replace("year1", year1).replace("year2", year2)
        return self.get_books(query)

    def get_book_by_isbn(self, isbn):
        string = str(isbn)
        query = self.getBook.replace("replace", string)
        dict = self.get_books(query)
        if len(dict) > 0:
            return dict[0]
        else:
            return None

    def update_seen(self, isbn):
        string = str(isbn)
        query = self.updateBook.replace("replace", string)
        self.db.update(query)

    def get_books_by_author(self, author):
        string = str(author)
        query = self.getBooksByAuthor.replace("replace", string)
        return self.get_books(query)
