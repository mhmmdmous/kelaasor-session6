class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def compare_grade(self, other):
       
        if self.grade > other.grade:
            print(self.name)
       
        elif self.grade < other.grade:
            print(other.name)
        
        elif self.grade == other.grade:
            print(f"{self.name}'s and {other.name}'s grades are Equall")

s1 = Student("Alice", 90)  
s2 = Student("Bob", 85)  
s1.compare_grade(s2)