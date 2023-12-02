import datetime
from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query="SELECT * from users;"
        results= connectToMySQL('users_schema').query_db(query)

        users = []
        for user in results:
            users.append(cls(user))
        
        return users
    
    @classmethod
    def add(cls,data):
        fname=data['fname']
        lname=data['lname']
        email=data['email']
        query = "INSERT INTO users (first_name,last_name,email) VALUES ('%s','%s','%s');" %(fname,lname,email)
        print(query)
        results= connectToMySQL('users_schema').query_db(query)
        return results
    
    @classmethod
    def update(cls,data):
        id=data['id']
        fname=data['fname']
        lname=data['lname']
        email=data['email']
        now=datetime.datetime.now()
        dt=now.strftime("%Y-%m-%d %H:%M:%S")
        query = "UPDATE users set first_name ='%s',last_name ='%s',email ='%s',updated_at='%s' WHERE id=%s;" %(fname,lname,email,dt,id)
        print(query)
        results= connectToMySQL('users_schema').query_db(query)
        return results
    
    @classmethod
    def one_user(cls,data):
        id=data['id']
        query= "SELECT * FROM users WHERE id=%s;" %id
        result=connectToMySQL('users_schema').query_db(query)
        print(result)
        return cls(result[0])
    
    @classmethod
    def remove(cls,data):
        
        query="DELETE FROM users WHERE id=%(id)s" 
        result=connectToMySQL('users_schema').query_db(query,data)
        return result
