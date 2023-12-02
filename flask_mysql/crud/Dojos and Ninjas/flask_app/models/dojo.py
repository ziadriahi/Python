from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas=[]

    @classmethod
    def all_dojos(cls):
        query="SELECT * FROM dojos;"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos=[]
        for dj in results:
            dojos.append(cls(dj))
        
        return dojos

    @classmethod
    def create(cls,data):
        query="INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result
    
    @classmethod
    def ninja_by_dojos_id(cls,data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON dojos.ID = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['updated_at'],
            }
            dojo.ninjas.append(Ninja(n))
        return dojo