import csv
from datetime import date

from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import FOAF, XSD
from datetime import datetime

author_id = 0
book_id = 0
publisher_id = 0
authors_l = []
publishers_l = []


#URI
base = Namespace("http://books.com/")
authors = Namespace("http://books.com/authors/")
books = Namespace("http://books.com/books/")
publishers = Namespace("http://books.com/publishers/")
predicate = Namespace("http://books.com/preds/")

#Predicates
title = predicate.has_title
isbn = predicate.has_isbn
pages = predicate.has_pages
language = predicate.has_language
published_on = predicate.published_on
rating = predicate.has_rating
rated_by = predicate.rated_by
written_by = predicate.written_by
published_by = predicate.published_by
pages = predicate.has_pages
name= predicate.has_name    # for authors and publishers
seen= predicate.has_seen    # for website users






with open('books.csv','r') as input:
    with open('books.nt','w') as output:
        reader = csv.DictReader(input)
        for row in reader:
            print(row)
            book = books[str(book_id)]
            output.write(book.n3()+" "+RDF.type.n3()+" "+FOAF.Document.n3()+".\n")

            output.write(book.n3()+" "+title.n3()+" "+Literal(row['title'],datatype=XSD.string).n3()+".\n")
            output.write(book.n3()+" "+isbn.n3()+" "+Literal(row['isbn'],datatype=XSD.string).n3()+".\n")
            output.write(book.n3()+" "+pages.n3()+" "+Literal(row['num_pages'],datatype=XSD.integer).n3()+".\n")
            output.write(book.n3()+" "+language.n3()+" "+Literal(row['language_code'],datatype=XSD.language).n3()+".\n")
            
            output.write(book.n3()+" "+rating.n3()+" "+Literal(row['average_rating'],datatype=XSD.float).n3()+".\n")
            output.write(book.n3()+" "+rated_by.n3()+" "+Literal(row['ratings_count'],datatype=XSD.integer).n3()+".\n")

            #convert date to datetime
            date = datetime.strptime(row['publication_date'], '%m/%d/%Y')
            output.write(book.n3()+" "+published_on.n3()+" "+Literal(date,datatype=XSD.date).n3()+".\n")
            




            for author in row['authors'].split('/'):

                if author not in authors_l:
                    authorm = authors[str(author_id)]
                    output.write(authorm.n3()+" "+RDF.type.n3()+" "+FOAF.Person.n3()+".\n")
                    output.write(authorm.n3()+" "+name.n3()+" "+Literal(author,datatype=XSD.string).n3()+".\n")
                    authors_l.append(author)

                    author_id += 1
                    output.write(book.n3()+" "+written_by.n3()+" "+authorm.n3()+".\n")
                else:
                    output.write(book.n3()+" "+written_by.n3()+" "+authors[str(authors_l.index(author))].n3()+".\n")

            if row['publisher'] not in publishers_l:
                publisher = publishers[str(publisher_id)]
                output.write(publisher.n3()+" "+RDF.type.n3()+" "+FOAF.Organization.n3()+".\n")
                output.write(publisher.n3()+" "+name.n3()+" "+Literal(row['publisher'],datatype=XSD.string).n3()+".\n")
                publishers_l.append(row['publisher'])
                publisher_id += 1
            else:
                publisher = publishers[str(publishers_l.index(row['publisher']))]
            output.write(book.n3()+" "+published_by.n3()+" "+publisher.n3()+".\n")

            # add row to seen or unseen books put all as unseen
            output.write(book.n3()+" "+seen.n3()+" "+Literal("unseen",datatype=XSD.string).n3()+".\n")


            book_id += 1





            



