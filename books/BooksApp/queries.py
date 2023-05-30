from .GraphDB import GraphDB
from SPARQLWrapper import SPARQLWrapper, JSON
import requests


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
        ?book pred:has_isbn ?isbn .
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
    
    SELECT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn ?co_author_name
    WHERE {
      # Subquery to find all books written by J.K. Rowling
      {
        SELECT ?book
        WHERE {
          ?book pred:written_by ?author .
          ?author pred:has_name "replace" .
        }
      }
    
      # Retrieve the details of the books and their co-authors
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
    
      # Retrieve the names of all co-authors for the book
      OPTIONAL {
        ?book pred:written_by ?co_author .
        ?co_author pred:has_name ?co_author_name .
        FILTER(?co_author_name != ?author_name)
      }
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
                    authors.append(i['author_name']['value'])
                    list[position]['author_name'] = authors

                #check if the genre is already in the list of genres
                if i['genre']['value'] not in genres:
                    #if not, add it
                    genres.append(i['genre']['value'])
                    list[position]['genre'] = genres

            else:
                dict = {}
                dict['title'] = i['title']['value']
                # save a list of authors
                dict['author_name'] = [i['author_name']['value']]
                dict['pages'] = i['pages']['value']
                dict['genre'] = [i['genre']['value']]

                dict['rating'] = i['rating']['value']
                dict['reviews'] = i['reviews']['value']
                dict['has_seen'] = i['has_seen']['value']
                if i['language']['value'] == 'eng':
                    dict['language'] = 'English'
                elif i['language']['value'] == 'spa':
                    dict['language'] = 'Spanish'
                elif i['language']['value'] == 'fre':
                    dict['language'] = 'French'
                elif i['language']['value'] == 'ger':
                    dict['language'] = 'German'
                elif i['language']['value'] == 'ita':
                    dict['language'] = 'Italian'
                elif i['language']['value'] == 'por':
                    dict['language'] = 'Portuguese'
                elif i['language']['value'] == 'tur':
                    dict['language'] = 'Turkish'
                elif i['language']['value'] == 'jpn':
                    dict['language'] = 'Japanese'
                elif i['language']['value'] == 'rus':
                    dict['language'] = 'Russian'
                elif i['language']['value'] == 'chi':
                    dict['language'] = 'Chinese'
                else:
                    dict['language'] = i['language']['value']

                dict['publisher_name'] = i['publisher_name']['value']
                dict['publication_date'] = i['publication_date']['value'].split('T')[0]
                dict['isbn'] = i['isbn']['value']

                list.append(dict)
                isbn_list.append(i['isbn']['value'])
        return list

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
        if keyword == '':
            return {}
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
    

    def get_author_image(author_name):
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(f"""
        SELECT ?image
        WHERE {{
            ?author wdt:P31 wd:Q5 .
            ?author wdt:P18 ?image .
            ?author rdfs:label "{author_name}"@en .
        }}
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        if len(results["results"]["bindings"]) > 0:
            return results["results"]["bindings"][0]["image"]["value"]
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery(f"""
        SELECT ?image
        WHERE {{
            ?author rdf:type dbo:Person .
            ?author dbo:thumbnail ?image .
            ?author rdfs:label "{author_name}"@en .
        }}
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        if len(results["results"]["bindings"]) > 0:
            return results["results"]["bindings"][0]["image"]["value"]
        
        url=f"https://www.googleapis.com/books/v1/volumes?q={author_name}&maxResults=1"
        response = requests.get(url)
        data = response.json()
        if "items" in data and data["items"]:
            volume_info = data["items"][0]["volumeInfo"]
            if "imageLinks" in volume_info and "thumbnail" in volume_info["imageLinks"]:
                return volume_info["imageLinks"]["thumbnail"]
        return None
    
    def get_book_image(book_title):
        url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&maxResults=1"
        response = requests.get(url)
        data = response.json()

        if "items" in data and data["items"]:
            volume_info = data["items"][0]["volumeInfo"]
            if "imageLinks" in volume_info and "thumbnail" in volume_info["imageLinks"]:
                return volume_info["imageLinks"]["thumbnail"]
        
        return None
    
    def get_book_genre(book_title):
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(f"""
        SELECT ?genreLabel WHERE {{
            ?book wdt:P31 wd:Q571 .
            ?book wdt:P136 ?genre .
            ?genre rdfs:label ?genreLabel .
            ?book rdfs:label "{book_title}"@en .
            FILTER (lang(?genreLabel) = 'en')
        }}
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        if len(results["results"]["bindings"]) > 0:
            return results["results"]["bindings"][0]["genreLabel"]["value"]

        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery(f"""
        PREFIX dct: <http://purl.org/dc/terms/>
        SELECT ?genreLabel WHERE {{
            ?book rdf:type dbo:Book .
            ?book dct:subject ?genre .
            ?genre rdfs:label ?genreLabel .
            ?book rdfs:label "{book_title}"@en .
            FILTER (lang(?genreLabel) = 'en')
        }}
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        if len(results["results"]["bindings"]) > 0:
            return results["results"]["bindings"][0]["genreLabel"]["value"]

        url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&maxResults=1"
        response = requests.get(url)
        data = response.json()

        if "items" in data and data["items"]:
            volume_info = data["items"][0]["volumeInfo"]
            if "categories" in volume_info and volume_info["categories"]:
                return volume_info["categories"][0]
            
        return None
    


        