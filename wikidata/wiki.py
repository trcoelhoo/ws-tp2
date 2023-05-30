from SPARQLWrapper import SPARQLWrapper, JSON
import requests

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

    
#test
print(get_author_image("Bill Bryson"))

#Search on wikidata and dbpedia to get the image of the book
def get_book_image(book_title):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(f"""
    SELECT ?image
    WHERE {{
        ?book wdt:P31 wd:Q571 .
        ?book wdt:P18 ?image .
        ?book rdfs:label "{book_title}"@en .
    }}
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    if len(results["results"]["bindings"]) > 0:
        return results["results"]["bindings"][0]["image"]["value"]
    else:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery(f"""
        SELECT ?image
        WHERE {{
            ?book rdf:type dbo:Book .
            ?book dbo:thumbnail ?image .
            ?book rdfs:label "{book_title}"@en .
        }}
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        if len(results["results"]["bindings"]) > 0:
            return results["results"]["bindings"][0]["image"]["value"]
        else:
            return None
        
#test
print(get_book_image("A Short History of Nearly Everything"))



def get_book_image(book_title):
    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&maxResults=1"
    response = requests.get(url)
    data = response.json()

    if "items" in data and data["items"]:
        volume_info = data["items"][0]["volumeInfo"]
        if "imageLinks" in volume_info and "thumbnail" in volume_info["imageLinks"]:
            return volume_info["imageLinks"]["thumbnail"]
    
    return None

# Test
book_title = "Artesia: Adventures in the Known World"
book_image = get_book_image(book_title)
if book_image:
    print("Book image URL:", book_image)
else:
    print("No book image found for the given book title.")


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

# Test
book_title = "Traders  Guns & Money: Knowns and Unknowns in the Dazzling World of Derivatives"
book_genre = get_book_genre(book_title)
if book_genre:
    print("Book genre:", book_genre)
else:
    print("No book genre found for the given book title.")


def get_minimal_age(book_title):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(f"""
    SELECT ?ageValue WHERE {{
        ?book wdt:P31 wd:Q571 .
        ?book wdt:P577 ?publicationDate .
        ?book wdt:P144 ?age .
        ?age wdt:P2043 ?ageValue .
        ?book rdfs:label "{book_title}"@en .
    }}
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    if len(results["results"]["bindings"]) > 0:
        return results["results"]["bindings"][0]["ageValue"]["value"]

    return None

# Test
book_title = "Traders  Guns & Money: Knowns and Unknowns in the Dazzling World of Derivatives"
minimal_age = get_minimal_age(book_title)
if minimal_age:
    print("Minimal age:", minimal_age)
else:
    print("No minimal age found for the given book title.")


#get minimal age from google api
def get_minimal_age(book_title):
    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&maxResults=1"
    response = requests.get(url)
    data = response.json()

    if "items" in data and data["items"]:
        volume_info = data["items"][0]["volumeInfo"]
        if "contentRating" in volume_info:
            return volume_info["contentRating"]
    
    return None

# Test
book_title = "Traders  Guns & Money: Knowns and Unknowns in the Dazzling World of Derivatives"
minimal_age = get_minimal_age(book_title)
if minimal_age:
    print("Minimal age:", minimal_age)
else:
    print("No minimal age found for the given book title.")
