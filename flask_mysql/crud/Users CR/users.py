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