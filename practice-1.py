class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def birthday(self):
        self.age += 1
        return self.age
        

p = Person("ali" , 25)
p.birthday()
print(p.age)