import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient
endpoint = "http://localhost:7200"
repo_name = "books"
client = ApiClient(endpoint=endpoint)
accessor = GraphDBApi(client)

# Query 1 - show the book with id 1
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT
    ?book

WHERE {
    books:1 pred:has_title ?title .
    ?book pred:has_title ?title .
}

"""

# Query 2 - show all the books that has "Harry Potter" as substring from its title (case insensitive)

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT
    ?book

WHERE {
    ?book pred:has_title ?title .
    FILTER regex(?title, "Harry Potter", "i")
}
"""

# Query 3 - show all the books that has "043935" on its ISBN

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT
    ?book

WHERE {
    ?book pred:has_isbn ?isbn .
    FILTER regex(?isbn, "^043935")
}

"""

# Query 4 - show all the books that has "Harry Potter" as substring from its title and starts with "043935" from its ISBN (case insensitive)

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT
    ?book

WHERE {
    ?book pred:has_title ?title .
    FILTER regex(?title, "Harry Potter", "i")
    ?book pred:has_isbn ?isbn .
    FILTER regex(?isbn, "^043935")
}

"""

# Query 5 - show all the books that has written by "Rowling" as substring from its author (case insensitive)

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX authors: <http://books.com/authors/>

SELECT ?book
WHERE {
    ?book pred:written_by ?author .
    ?author pred:has_name ?name .
    FILTER regex(?name, "Rowling", "i")
}

"""

# Query 6 - show all the books that has written by "Rowling" as substring from its author and has "Harry Potter" as substring from its title (case insensitive)

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX authors: <http://books.com/authors/>

SELECT ?book
WHERE {
    ?book pred:written_by ?author .
    ?author pred:has_name ?name .
    FILTER regex(?name, "Rowling" , "i")
    ?book pred:has_title ?title .
    FILTER regex(?title, "Harry Potter", "i")
}


"""

# Query 7 - show all the books that its written on turkish language (xsd:language)

query = """
PREFIX preds: <http://books.com/preds/>
PREFIX books: <http://books.com/books/>
SELECT ?book
WHERE {
    ?book preds:has_language ?language .
    FILTER (?language = "tur"^^xsd:language)
}

"""

# Query 8 - show all the books that was published after 2019  and before 2020

query = """
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
    FILTER (?publication_date > "2017-01-01"^^xsd:date && ?publication_date < "2020-01-01"^^xsd:date)
}


"""

# Query 9 - show all the books that was more than 3000 pages 

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT ?book
WHERE {
    ?book pred:has_pages ?pages .
    FILTER (xsd:integer(?pages) > 3000)
}



"""

# Query 10 - show all the books that as rating more than 3.5 and less than 4.5

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT ?book
WHERE {
    ?book pred:has_rating ?rating .
    FILTER (xsd:decimal(?rating) > 3.5 && xsd:decimal(?rating) < 4.5)
}


"""

# Query 11 - show all the books was published by "USA" as substring from its publisher (case insensitive)

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX publishers: <http://books.com/publishers/>
SELECT ?book
WHERE {
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?name .
    FILTER regex(?name, "USA", "i")
}

"""

# Query 12 - remove has_seen property from all books and add has_seen_by property to all books

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_seen_by ?seen .
}
INSERT {
    ?book pred:has_seen "false"^^xsd:boolean .
}
WHERE {
    ?book pred:has_seen_by ?seen .
}
"""

#Query 13 - mark a book as seen

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    books:1 pred:has_seen "false"^^xsd:boolean .
}
INSERT {
    books:1 pred:has_seen "true"^^xsd:boolean .
}
WHERE {
    books:1 pred:has_seen "false"^^xsd:boolean .
}
"""

# Query 14 - show all the books that has seen

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT ?book
WHERE {
    ?book pred:has_seen "true"^^xsd:boolean .
}

"""

# Query 15 - show all the books that has not seen

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT ?book
WHERE {
    ?book pred:has_seen "false"^^xsd:boolean .
}

"""

# Query 16 - mark a book as not seen

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    books:1 pred:has_seen "true"^^xsd:boolean .
}
INSERT {
    books:1 pred:has_seen "false"^^xsd:boolean .
}
WHERE {
    books:1 pred:has_seen "true"^^xsd:boolean .
}
"""
# Query 17 - Search for a book by its title or isbn or author name or publisher name (case insensitive) and show the results without duplicates


query = """
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
    FILTER regex(?title, "Harry Potter", "i")
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
    FILTER regex(?isbn, "Harry Potter", "i")
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
    FILTER regex(?author_name, "Harry Potter", "i")
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
    FILTER regex(?publisher_name, "Harry Potter", "i")
    }
}



"""

# Query 18 - add genres to the books based on the following rules:
# 1. If the book has more than 1000 pages, add "long" genre
# 2. If the book has more than 4.5 rating, add "good" genre
# 3. If the book has more than 1000 pages and more than 4.5 rating, add "long_good" genre
# 5. If the book has more than 1000 pages and less than 3.5 rating, add "long_bad" genre
# 6. If the book has less than 1000 pages and more than 4.5 rating, add "short_good" genre
# 7. If the book has less than 1000 pages and less than 3.5 rating, add "short_bad" genre
# 8. If the book has less than 1000 pages, add "short" genre
# 9. If the book has less than 3.5 rating, add "bad" genre
# 10. If the book has more than 500 reviews, add "popular" genre

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "long" .
}
WHERE {
    ?book pred:has_pages ?pages .
    FILTER (xsd:integer(?pages) > 1000)
}
"""

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "good" .
}
WHERE {
    ?book pred:has_rating ?rating .
    FILTER (xsd:decimal(?rating) > 4.5)
}
"""

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "long_good" .
}
WHERE {
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    FILTER (xsd:integer(?pages) > 1000 && xsd:decimal(?rating) > 4.5)
}
"""

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "long_bad" .
}
WHERE {
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    FILTER (xsd:integer(?pages) > 1000 && xsd:decimal(?rating) < 3.5)
}
"""

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "short_good" .
}
WHERE {
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    FILTER (xsd:integer(?pages) < 1000 && xsd:decimal(?rating) > 4.5)
}
"""

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "short_bad" .
}
WHERE {
    ?book pred:has_pages ?pages .
    ?book pred:has_rating ?rating .
    FILTER (xsd:integer(?pages) < 1000 && xsd:decimal(?rating) < 3.5)
}
"""

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "short" .
}
WHERE {
    ?book pred:has_pages ?pages .
    FILTER (xsd:integer(?pages) < 1000)
}
"""

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "bad" .
}
WHERE {
    ?book pred:has_rating ?rating .
    FILTER (xsd:decimal(?rating) < 3.5)
}
"""

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre ?genre .
}
INSERT {
    ?book pred:has_genre "popular" .
}

WHERE {
    ?book pred:rated_by ?reviews .
    FILTER (xsd:integer(?reviews) > 10000)
}
"""

# Query 19 - find all books that have "short" genre and "good" genre
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT ?book
WHERE {
    ?book pred:has_genre "short" .
    ?book pred:has_genre "good" .
}
"""

# Query 20 - filter books by the shortest page count and return ordered by the shortest page count
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT ?book
WHERE {
    ?book pred:has_pages ?pages .
}
ORDER BY ASC(?pages)
"""

#Query 21 -get number of books that have "short" genre
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT (COUNT(?book) AS ?count)
WHERE {
    ?book pred:has_genre "short" .
}
"""

# Query 22 - get number of books that have "short" genre and "good" genre
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT (COUNT(?book) AS ?count)
WHERE {
    ?book pred:has_genre "short_good" .
}
"""

# Query 23 - get number of good books
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT (COUNT(?book) AS ?count)
WHERE {
    ?book pred:has_genre "good" .
}
"""

# Query 24 - get number of bad books
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT (COUNT(?book) AS ?count)
WHERE {
    ?book pred:has_genre "bad" .
}
"""

# Query 25 - get number of popular books
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT (COUNT(?book) AS ?count)
WHERE {
    ?book pred:has_genre "popular" .
}
"""

# Query 26 - get number of long books
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT (COUNT(?book) AS ?count)
WHERE {
    ?book pred:has_genre "long" .
}
"""

# Query 27 - get number of books
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT (COUNT(?book) AS ?count)
WHERE {
    ?book pred:has_genre ?genre .
}
"""

# Query 28 - get short books titles, authors names, pages, genres, ratings, number of reviews, has seen, language, publisher name, publication date and isbn (distinct and unite auhtors and genres)
query = """
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

# Query 29 - update genre of books that have "short" genre for less than 300 pages

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre "short" .
}
INSERT {
    ?book pred:has_genre "long" .
}
WHERE {
    ?book pred:has_genre "short" .
    ?book pred:has_pages ?pages .
    FILTER (xsd:integer(?pages) > 300)
}
"""

# Query 30 - update genre of books that have "good genre for more than4.0
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE {
    ?book pred:has_genre "bad" .
}
INSERT {
    ?book pred:has_genre "good" .
}
WHERE {
    ?book pred:has_genre "bad" .
    ?book pred:has_rating ?rating .
    FILTER (xsd:decimal(?rating) > 4.0)
}
"""

#Get seen books (boolean value)
query = """
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

#Get books from J.K. Rowling (author name) and the rest of the authors from the same book
query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>

SELECT ?title ?author_name ?pages ?genre ?rating ?reviews ?has_seen ?language ?publisher_name ?publication_date ?isbn ?co_author_name
WHERE {
  # Subquery to find all books written by J.K. Rowling
  {
    SELECT ?book
    WHERE {
      ?book pred:written_by ?author .
      ?author pred:has_name "J.K. Rowling" .
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



payload_query = {"query": query}
res = accessor.sparql_select(body=payload_query,
repo_name=repo_name)
res = json.loads(res)

list=[]
for i in res['results']['bindings']:

    #check if the book is already in the list and if it is, add the author to the list of authors and the genre to the list of genres if it is not already there
    if i['isbn']['value'] in [x['isbn'] for x in list]:
        for x in list:
            if x['isbn']==i['isbn']['value']:
                if i['author_name']['value'] not in x['author_name']:
                    x['author_name']=x['author_name']+", "+i['author_name']['value']
                if i['genre']['value'] not in x['genre']:
                    x['genre']=x['genre']+", "+i['genre']['value']
    else:
        dict={}
        dict['title']=i['title']['value']
        dict['author_name']=i['author_name']['value']
        dict['pages']=i['pages']['value']
        dict['genre']=i['genre']['value']
        dict['rating']=i['rating']['value']
        dict['reviews']=i['reviews']['value']
        dict['has_seen']=i['has_seen']['value']
        dict['language']=i['language']['value']
        dict['publisher_name']=i['publisher_name']['value']
        dict['publication_date']=i['publication_date']['value']
        dict['isbn']=i['isbn']['value']

        list.append(dict)

print(list)

