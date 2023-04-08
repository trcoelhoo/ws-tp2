from BooksApp.GraphDB import GraphDB


class Queries:

    #Get the number of short books (less than 1000 pages)
    nShortBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "short" .
    }
    """

    #Get short books
    shortBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT ?book
    WHERE {
        ?book pred:has_genre "short" .
    }
    """

    #Get the number of books with a rating of 4.5 or higher
    nGoodBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "good" .
    }
    """

    #Get good books
    goodBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT ?book
    WHERE {
        ?book pred:has_genre "good" .
    }
    """

    #Get the number of books with a rating lower than 4.5
    nBadBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "bad" .
    }
    """

    #Get bad books
    badBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT ?book
    WHERE {
        ?book pred:has_genre "bad" .
    }
    """

    #Get the number of books long books (more than 1000 pages)
    nLongBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "long" .
    }
    """

    #Get long books
    longBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT ?book
    WHERE {
        ?book pred:has_genre "long" .
    }
    """

    #Get the number of popular books (more than 10000 ratings)
    nPopularBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre "popular" .
    }
    """

    #Get popular books
    popularBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT ?book
    WHERE {
        ?book pred:has_genre "popular" .
    }
    """

    #Get the number of books
    nBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_genre ?genre .
    }
    """

    #Get the number of books seen
    nSeenBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_seen "true"^^xsd:boolean .
    }
    """

    #Get seen books
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


    #Get all books
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

    #Search for a book by title, author, isbn or publisher
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

    #Search by year
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

    def __init__(self, endpoint, repo_name):
        self.endpoint = endpoint
        self.repo_name = repo_name
        self.db = GraphDB(endpoint, repo_name)


    def get_number_short_books(self):
        response = self.db.query(self.nShortBooks)
        return response[0]['count']['value']

    def get_number_good_books(self):
        response = self.db.query(self.nGoodBooks)
        return response[0]['count']['value']

    def get_number_bad_books(self):
        response = self.db.query(self.nBadBooks)
        return response[0]['count']['value']

    def get_number_long_books(self):
        response = self.db.query(self.nLongBooks)
        return response[0]['count']['value']

    def get_number_popular_books(self):
        response = self.db.query(self.nPopularBooks)
        return response[0]['count']['value']

    def get_number_books(self):
        response = self.db.query(self.nBooks)
        return response[0]['count']['value']

    def get_books(self, query):
        response = self.db.query(query)
        list = []
        isbn_list = []
        for i in response:

            # check if the book is already in the list and if it is, add the author to the list of authors and the genre to the list of genres if it is not already there
            if i['isbn']['value'] in isbn_list:
                #get position of the book in the list
                position = isbn_list.index(i['isbn']['value'])
                #get the list of authors
                authors = list[position]['author_name']
                #get the list of genres
                genres = list[position]['genre']
                #check if the author is already in the list of authors
                if i['author_name']['value'] not in authors:
                    #if not, add it
                    authors= list[position]['author_name']+","+i['author_name']['value']
                #check if the genre is already in the list of genres
                if i['genre']['value'] not in genres:
                    #if not, add it
                    genres= list[position]['genre']+","+i['genre']['value']

            else:
                dict = {}
                dict['title'] = i['title']['value']
                dict['author_name'] = i['author_name']['value']
                dict['pages'] = i['pages']['value']
                dict['genre'] = i['genre']['value']
                dict['rating'] = i['rating']['value']
                dict['reviews'] = i['reviews']['value']
                dict['has_seen'] = i['has_seen']['value']
                dict['language'] = i['language']['value']
                dict['publisher_name'] = i['publisher_name']['value']
                dict['publication_date'] = i['publication_date']['value']
                dict['isbn'] = i['isbn']['value']

                list.append(dict)
                isbn_list.append(i['isbn']['value'])

        return list

    def get_short_books(self):
        return self.get_books(self.shortBooks)

    def get_good_books(self):
        return self.get_books(self.goodBooks)

    def get_bad_books(self):
        return self.get_books(self.badBooks)

    def get_long_books(self):
        return self.get_books(self.longBooks)

    def get_popular_books(self):
        return self.get_books(self.popularBooks)

    def get_all_books(self):
        return self.get_books(self.allBooks)

    def search_book(self, keyword):
        query = self.searchBook.replace("toSearch", keyword)
        return self.get_books(query)

    def search_year(self, year1, year2):
        query = self.searchYear.replace("year1", year1).replace("year2", year2)
        return self.get_books(query)

    def get_number_seen_books(self):
        response = self.db.query(self.nSeenBooks)
        return response[0]['count']['value']

    def get_seen_books(self):
        query = self.seenBooks
        return self.get_books(query)








