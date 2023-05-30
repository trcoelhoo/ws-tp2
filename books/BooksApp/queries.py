from .GraphDB import GraphDB
from SPARQLWrapper import SPARQLWrapper, JSON
import requests


class Queries:

    # Get the number of short books (less than 1000 pages)
    nShortBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book rdf:type books:Short .
    }
    """

    # Get short books
    shortBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
    ?book pred:has_title ?title .
    ?book pred:written_by ?author .
    ?author pred:has_name ?author_name .
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    ?book pred:rated_by ?reviews .
    ?book pred:has_seen ?has_seen .
    ?book pred:has_language ?language .
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?publisher_name .
    ?book pred:published_on ?publication_date .
    ?book pred:has_isbn ?isbn .
    ?book rdf:type books:Short .

    # Include inferred genres based on rules
    OPTIONAL {
            {
            ?book rdf:type books:Long .
            BIND("Long" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Short .
            BIND("Short" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Good .
            BIND("Good" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Bad .
            BIND("Bad" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Popular .
            BIND("Popular" AS ?genre)
            }
    }
        

    }
    """

    # Get the number of books with a rating of 4.5 or higher
    nGoodBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book rdf:type books:Good .
    }
    
    """

    # Get good books
    goodBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
    ?book pred:has_title ?title .
    ?book pred:written_by ?author .
    ?author pred:has_name ?author_name .
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    ?book pred:rated_by ?reviews .
    ?book pred:has_seen ?has_seen .
    ?book pred:has_language ?language .
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?publisher_name .
    ?book pred:published_on ?publication_date .
    ?book pred:has_isbn ?isbn .
    ?book rdf:type books:Good .

    # Include inferred genres based on rules
    OPTIONAL {
            {
            ?book rdf:type books:Long .
            BIND("Long" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Short .
            BIND("Short" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Good .
            BIND("Good" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Bad .
            BIND("Bad" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Popular .
            BIND("Popular" AS ?genre)
            }
    }
        

    }
    """

    # Get the number of books with a rating lower than 4.5
    nBadBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book rdf:type books:Bad .
    }
    
    """

    # Get bad books
    badBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
    ?book pred:has_title ?title .
    ?book pred:written_by ?author .
    ?author pred:has_name ?author_name .
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    ?book pred:rated_by ?reviews .
    ?book pred:has_seen ?has_seen .
    ?book pred:has_language ?language .
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?publisher_name .
    ?book pred:published_on ?publication_date .
    ?book pred:has_isbn ?isbn .
    ?book rdf:type books:Bad .

    # Include inferred genres based on rules
    OPTIONAL {
            {
            ?book rdf:type books:Long .
            BIND("Long" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Short .
            BIND("Short" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Good .
            BIND("Good" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Bad .
            BIND("Bad" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Popular .
            BIND("Popular" AS ?genre)
            }
    }
        

    }
    """

    # Get the number of books long books (more than 1000 pages)
    nLongBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book rdf:type books:Long .
    }
    """

    # Get long books
    longBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
    ?book pred:has_title ?title .
    ?book pred:written_by ?author .
    ?author pred:has_name ?author_name .
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    ?book pred:rated_by ?reviews .
    ?book pred:has_seen ?has_seen .
    ?book pred:has_language ?language .
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?publisher_name .
    ?book pred:published_on ?publication_date .
    ?book pred:has_isbn ?isbn .
    ?book rdf:type books:Long .

    # Include inferred genres based on rules
    OPTIONAL {
            {
            ?book rdf:type books:Long .
            BIND("Long" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Short .
            BIND("Short" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Good .
            BIND("Good" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Bad .
            BIND("Bad" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Popular .
            BIND("Popular" AS ?genre)
            }
    }
        

    }
    """

    # Get the number of popular books (more than 10000 ratings)
    nPopularBooks = """
    PREFIX books: <http://books.com/books/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book rdf:type books:Popular .
    }
    
    """

    # Get popular books
    popularBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
    ?book pred:has_title ?title .
    ?book pred:written_by ?author .
    ?author pred:has_name ?author_name .
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    ?book pred:rated_by ?reviews .
    ?book pred:has_seen ?has_seen .
    ?book pred:has_language ?language .
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?publisher_name .
    ?book pred:published_on ?publication_date .
    ?book pred:has_isbn ?isbn .
    ?book rdf:type books:Popular .

    # Include inferred genres based on rules
    OPTIONAL {
            {
            ?book rdf:type books:Long .
            BIND("Long" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Short .
            BIND("Short" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Good .
            BIND("Good" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Bad .
            BIND("Bad" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Popular .
            BIND("Popular" AS ?genre)
            }
    }
        

    }
    """

    # Get the number of books
    nBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_isbn ?isbn .
    }
    """

    # Get the number of books seen
    nSeenBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT (COUNT(?book) AS ?count)
    WHERE {
        ?book pred:has_seen "seen" .
    }

    """

    # Get seen books
    seenBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_seen "seen" .
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
            # Include inferred genres based on rules
        OPTIONAL {
            {
            ?book rdf:type books:Long .
            BIND("Long" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Short .
            BIND("Short" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Good .
            BIND("Good" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Bad .
            BIND("Bad" AS ?genre)
            }
            UNION
            {
            ?book rdf:type books:Popular .
            BIND("Popular" AS ?genre)
            }
        }
        }
    """

    # Get all books
    allBooks = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
    ?book pred:has_title ?title .
    ?book pred:written_by ?author .
    ?author pred:has_name ?author_name .
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    ?book pred:rated_by ?reviews .
    ?book pred:has_seen ?has_seen .
    ?book pred:has_language ?language .
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?publisher_name .
    ?book pred:published_on ?publication_date .
    ?book pred:has_isbn ?isbn .

    # Include inferred genres based on rules
    OPTIONAL {
        {
        ?book rdf:type books:Long .
        BIND("Long" AS ?genre)
        }
        UNION
        {
        ?book rdf:type books:Short .
        BIND("Short" AS ?genre)
        }
        UNION
        {
        ?book rdf:type books:Good .
        BIND("Good" AS ?genre)
        }
        UNION
        {
        ?book rdf:type books:Bad .
        BIND("Bad" AS ?genre)
        }
        UNION
        {
        ?book rdf:type books:Popular .
        BIND("Popular" AS ?genre)
        }
    }
    }


    """

    # Search for a book by title, author, isbn or publisher
    searchBook = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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
            ?book pred:has_rating ?rating .
            ?book pred:rated_by ?reviews .
            ?book pred:has_seen ?has_seen .
            ?book pred:has_language ?language .
            ?book pred:published_by ?publisher .
            ?publisher pred:has_name ?publisher_name .
            ?book pred:published_on ?publication_date .
            ?book pred:has_isbn ?isbn .
            OPTIONAL {
                {
                    ?book rdf:type books:Long .
                    BIND("Long" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Short .
                    BIND("Short" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Good .
                    BIND("Good" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Bad .
                    BIND("Bad" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Popular .
                    BIND("Popular" AS ?genre)
                }
            }
            FILTER regex(?title, "toSearch", "i")
        }
        UNION
        {
            ?book pred:has_title ?title .
            ?book pred:written_by ?author .
            ?author pred:has_name ?author_name .
            ?book pred:has_pages ?pages .
            ?book pred:has_rating ?rating .
            ?book pred:rated_by ?reviews .
            ?book pred:has_seen ?has_seen .
            ?book pred:has_language ?language .
            ?book pred:published_by ?publisher .
            ?publisher pred:has_name ?publisher_name .
            ?book pred:published_on ?publication_date .
            ?book pred:has_isbn ?isbn .
            OPTIONAL {
                {
                    ?book rdf:type books:Long .
                    BIND("Long" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Short .
                    BIND("Short" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Good .
                    BIND("Good" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Bad .
                    BIND("Bad" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Popular .
                    BIND("Popular" AS ?genre)
                }
            }
            FILTER regex(?isbn, "toSearch", "i")
        }
        UNION
        {
            ?book pred:has_title ?title .
            ?book pred:written_by ?author .
            ?author pred:has_name ?author_name .
            ?book pred:has_pages ?pages .
            ?book pred:has_rating ?rating .
            ?book pred:rated_by ?reviews .
            ?book pred:has_seen ?has_seen .
            ?book pred:has_language ?language .
            ?book pred:published_by ?publisher .
            ?publisher pred:has_name ?publisher_name .
            ?book pred:published_on ?publication_date .
            ?book pred:has_isbn ?isbn .
            OPTIONAL {
                {
                    ?book rdf:type books:Long .
                    BIND("Long" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Short .
                    BIND("Short" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Good .
                    BIND("Good" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Bad .
                    BIND("Bad" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Popular .
                    BIND("Popular" AS ?genre)
                }
            }
            FILTER regex(?author_name, "toSearch", "i")
        }
        UNION
        {
            ?book pred:has_title ?title .
            ?book pred:written_by ?author .
            ?author pred:has_name ?author_name .
            ?book pred:has_pages ?pages .
            ?book pred:has_rating ?rating .
            ?book pred:rated_by ?reviews .
            ?book pred:has_seen ?has_seen .
            ?book pred:has_language ?language .
            ?book pred:published_by ?publisher .
            ?publisher pred:has_name ?publisher_name .
            ?book pred:published_on ?publication_date .
            ?book pred:has_isbn ?isbn .
            OPTIONAL {
                {
                    ?book rdf:type books:Long .
                    BIND("Long" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Short .
                    BIND("Short" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Good .
                    BIND("Good" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Bad .
                    BIND("Bad" AS ?genre)
                }
                UNION
                {
                    ?book rdf:type books:Popular .
                    BIND("Popular" AS ?genre)
                }
            }
            FILTER regex(?publisher_name, "toSearch", "i")
        }
    }

    """

    # Search by year
    searchYear = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    
    SELECT DISTINCT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
        ?book pred:has_title ?title .
        ?book pred:written_by ?author .
        ?author pred:has_name ?author_name .
        ?book pred:has_pages ?pages .
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
      
        # Include inferred genres based on rules
        OPTIONAL {
            {
                ?book rdf:type books:Long .
                BIND("Long" AS ?genre)
            }
            UNION
            {
                ?book rdf:type books:Short .
                BIND("Short" AS ?genre)
            }
            UNION
            {
                ?book rdf:type books:Good .
                BIND("Good" AS ?genre)
            }
            UNION
            {
                ?book rdf:type books:Bad .
                BIND("Bad" AS ?genre)
            }
            UNION
            {
                ?book rdf:type books:Popular .
                BIND("Popular" AS ?genre)
            }
        }
        
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
        ?book pred:has_rating ?rating .
        ?book pred:rated_by ?reviews .
        ?book pred:has_seen ?has_seen .
        ?book pred:has_language ?language .
        ?book pred:published_by ?publisher .
        ?publisher pred:has_name ?publisher_name .
        ?book pred:published_on ?publication_date .
        ?book pred:has_isbn ?isbn .
        FILTER regex(?isbn, "replace", "i")
        # Include inferred genres based on rules
      OPTIONAL {
        {
          ?book rdf:type books:Long .
          BIND("Long" AS ?genre)
        }
        UNION
        {
          ?book rdf:type books:Short .
          BIND("Short" AS ?genre)
        }
        UNION
        {
          ?book rdf:type books:Good .
          BIND("Good" AS ?genre)
        }
        UNION
        {
          ?book rdf:type books:Bad .
          BIND("Bad" AS ?genre)
        }
        UNION
        {
          ?book rdf:type books:Popular .
          BIND("Popular" AS ?genre)
        }
      }
    }
    
    """

    # Updates the book to the inverse of the current value
    updateBook = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    DELETE {
      ?book pred:has_seen ?has_seen .
    }
    INSERT {
      ?book pred:has_seen ?new_has_seen .
      ?book rdf:type books:Seen .
    }
    WHERE {
      ?book pred:has_isbn ?isbn .
      ?book pred:has_seen ?has_seen .
      BIND(IF(?has_seen = "seen", "unseen", "seen") AS ?new_has_seen)
      FILTER (?isbn = "replace")
    }

    """

    # Get books from author
    getBooksByAuthor = """
    PREFIX books: <http://books.com/books/>
    PREFIX pred: <http://books.com/preds/>

    SELECT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn
    WHERE {
    # Subquery to find all books written by the author
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
    ?book pred:has_rating ?rating .
    ?book pred:rated_by ?reviews .
    ?book pred:has_seen ?has_seen .
    ?book pred:has_language ?language .
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?publisher_name .
    ?book pred:published_on ?publication_date .
    ?book pred:has_isbn ?isbn .

    OPTIONAL {
        {
        ?book rdf:type books:Long .
        BIND("Long" AS ?genre)
        }
        UNION
        {
        ?book rdf:type books:Short .
        BIND("Short" AS ?genre)
        }
        UNION
        {
        ?book rdf:type books:Good .
        BIND("Good" AS ?genre)
        }
        UNION
        {
        ?book rdf:type books:Bad .
        BIND("Bad" AS ?genre)
        }
        UNION
        {
        ?book rdf:type books:Popular .
        BIND("Popular" AS ?genre)
        }
    }
    }

    
    """

    create_long_books = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX book: <http://books.com/books/>
        PREFIX bookp: <http://books.com/preds/>
            
        INSERT {
            ?X rdf:type book:Long .
        }
        WHERE {
            ?X rdf:type book:Book .
            ?X bookp:has_pages ?N .
            FILTER (?N >= 1000)
        }

    """

    create_short_books = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX book: <http://books.com/books/>
            PREFIX bookp: <http://books.com/preds/>

            INSERT {
                ?X rdf:type book:Short .
            }
            WHERE {
                ?X rdf:type book:Book .
                ?X bookp:has_pages ?N .
                FILTER (?N < 1000)
            }

        """

    create_good_books = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX book: <http://books.com/books/>
            PREFIX bookp: <http://books.com/preds/>
            
            INSERT {
                ?X rdf:type book:Good .
            }
            WHERE {
                ?X rdf:type book:Book .
                ?X bookp:has_rating ?N .
                FILTER (?N >= 4)
            }
            
        """

    create_bad_books = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>   
            PREFIX book: <http://books.com/books/>
            PREFIX bookp: <http://books.com/preds/>
                
            INSERT {
                ?X rdf:type book:Bad .
            }
            WHERE {
                ?X rdf:type book:Book .
                ?X bookp:has_rating ?N .
                FILTER (?N < 4)
            }
            
        """
    create_popular_books = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX book: <http://books.com/books/>
            PREFIX bookp: <http://books.com/preds/>
            
            INSERT {
                ?X rdf:type book:Popular .
            }
            WHERE {
                ?X rdf:type book:Book .
                ?X bookp:rated_by ?N .
                FILTER (?N >= 10000)
            }
            
        """

    create_seen_books = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX book: <http://books.com/books/>
            PREFIX bookp: <http://books.com/preds/>
            
            INSERT {
                ?X rdf:type book:Seen .
            }
            WHERE {
                ?X rdf:type book:Book .
                ?X bookp:has_seen ?N .
                FILTER (?N = "true"^^xsd:boolean)
            }
            
        """




    def __init__(self, endpoint, repo_name):
        self.endpoint = endpoint
        self.repo_name = repo_name
        self.db = GraphDB(endpoint, repo_name)
        self.db.create(self.create_short_books)
        self.db.create(self.create_long_books)
        self.db.create(self.create_good_books)
        self.db.create(self.create_bad_books)
        self.db.create(self.create_popular_books)
        self.db.create(self.create_seen_books)
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
        self.db.create(self.create_long_books)
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
            book = dict[0]
            book['book_image'] = self.get_book_image(book['title'])
            return book

        else:
            return None



    def update_seen(self, isbn):
        string = str(isbn)
        query = self.updateBook.replace("replace", string)
        #update seen in the database
        self.db.create(self.create_seen_books)
        self.db.update(query)

    def get_author(self, author):
        string = str(author)
        query = self.getBooksByAuthor.replace("replace", string)
        author = dict()
        author['author_name'] = string
        author['books'] = self.get_books(query)
        if len(author['books']) > 0:
            author['author_image'] = self.get_author_image(author['author_name'])

        return author


    def get_author_image(self, author_name):
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
    
    def get_book_image(self, book_title):
        url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&maxResults=1"
        response = requests.get(url)
        data = response.json()

        if "items" in data and data["items"]:
            volume_info = data["items"][0]["volumeInfo"]
            if "imageLinks" in volume_info and "thumbnail" in volume_info["imageLinks"]:
                return volume_info["imageLinks"]["thumbnail"]
        
        return None
    
    def get_book_genre(self, book_title):
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

    def get_author_info(self, author_name):
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(f"""
        SELECT ?birthDate ?occupationLabel ?genreLabel WHERE {{
            ?author wdt:P31 wd:Q5 .
            ?author wdt:P569 ?birthDate .
            ?author wdt:P106 ?occupation .
            ?author wdt:P136 ?genre .
            ?occupation rdfs:label ?occupationLabel .
            ?genre rdfs:label ?genreLabel .
            ?author rdfs:label "{author_name}"@en .
            FILTER (lang(?occupationLabel) = 'en')
            FILTER (lang(?genreLabel) = 'en')
        }}
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        if len(results["results"]["bindings"]) > 0:
            return results["results"]["bindings"][0]

        return None


        