from flask_app.config.mysqlconnection import DB,connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self,data):
        self.id=data["id"]
        self.title=data["title"]
        self.num_of_pages=data["num_of_pages"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.authors=[]
    
    @classmethod
    def save(cls,data):
        query="INSERT INTO books (title,num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        result=connectToMySQL(DB).query_db(query,data)
        return result
    @classmethod
    def get_all(cls):
        query="SELECT * FROM books;"
        result=connectToMySQL(DB).query_db(query)
        books=[]
        for row in result:
            books.append(cls(row))
        return books
    
    @classmethod
    def unfavorited_books(cls,data):
        query="SELECT * FROM books WHERE id NOT IN (SELECT book_id FROM favorites WHERE author_id=%(id)s);"
        results=connectToMySQL(DB).query_db(query,data)
        books=[]
        for row in results:
            books.append(cls(row))
        return books
    
    @classmethod
    def add_favorite(cls,data):
        query="INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        result=connectToMySQL(DB).query_db(query,data)
        return result
    
    @classmethod
    def get_by_id(cls,data):
        query="SELECT * FROM books LEFT JOIN favorites ON books.id=favorites.book_id LEFT JOIN authors ON authors.id=favorites.author_id WHERE books.id=%(id)s;"
        results=connectToMySQL(DB).query_db(query,data)
        book= cls(results[0])
        for row in results:
            if row['authors.id'] == None:
                break
            
            data={
                "id":row['authors.id'],
                "full_name":row['full_name'],
                "created_at":row['authors.created_at'],
                "updated_at":row['authors.updated_at']
                }
            book.authors.append(author.Author(data))
        
        return book