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

# Query 2 - show all the books that has "Harry Potter" as substring from its title

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT
    ?book

WHERE {
    ?book pred:has_title ?title .
    FILTER regex(?title, "Harry Potter")
}

"""

# Query 3 - show all the books that starts with "043935" from its ISBN

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

# Query 4 - show all the books that has "Harry Potter" as substring from its title and starts with "043935" from its ISBN

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT
    ?book

WHERE {
    ?book pred:has_title ?title .
    FILTER regex(?title, "Harry Potter")
    ?book pred:has_isbn ?isbn .
    FILTER regex(?isbn, "^043935")
}

"""

# Query 5 - show all the books that has written by "Rowling" as substring from its author

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX authors: <http://books.com/authors/>

SELECT ?book
WHERE {
    ?book pred:written_by ?author .
    ?author pred:has_name ?name .
    FILTER regex(?name, "Rowling")
}

"""

# Query 6 - show all the books that has written by "Rowling" as substring from its author and has "Harry Potter" as substring from its title

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX authors: <http://books.com/authors/>

SELECT ?book
WHERE {
    ?book pred:written_by ?author .
    ?author pred:has_name ?name .
    FILTER regex(?name, "Rowling")
    ?book pred:has_title ?title .
    FILTER regex(?title, "Harry Potter")
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

# Query 8 - show all the books that was published after 2019 

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT ?book
WHERE {
    ?book pred:published_on ?date .
    FILTER (?date > "2019-01-01"^^xsd:date)
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

# Query 10 - show all the books that as rating more than 4.9 

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
SELECT ?book
WHERE {
    ?book pred:has_rating ?rating .
    FILTER (xsd:decimal(?rating) > 4.9)
}


"""

# Query 11 - show all the books was published by "USA" as substring from its publisher

query = """
PREFIX books: <http://books.com/books/>
PREFIX pred: <http://books.com/preds/>
PREFIX publishers: <http://books.com/publishers/>
SELECT ?book
WHERE {
    ?book pred:published_by ?publisher .
    ?publisher pred:has_name ?name .
    FILTER regex(?name, "USA")
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

payload_query = {"query": query}
res = accessor.sparql_select(body=payload_query,
repo_name=repo_name)
res = json.loads(res)
for b in res["results"]["bindings"]:
    print(b["book"]["value"])
