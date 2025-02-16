import hashlib  

class User:  
    user_list = []  

    def __init__(self, username: str, password: str):  
        self.username = username  
        self.password = self.hash_password(password)  
        self.add_user()  

    def hash_password(self, password: str):  
        return hashlib.sha256(password.encode()).hexdigest()  

    def add_user(self):  
        User.user_list.append((self.username, self.password))  
  
    def authenticate(self, username: str, password: str):  
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  
          
        if self.username == username and self.password == hashed_password:  
                  
                return True  
        else:
                return False
              

# Create user objects
user_list = []
user_list.append(User("Faezeh", "123456"))
user_list.append(User("Fariborz", "ffborz"))
user_list.append(User("Hamed", "kelaasor"))


for user in user_list:
    print(user.authenticate("Hamed", "kelaasor") ) # prints 3 False