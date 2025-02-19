class Teacher:
    def __init__(self, name):
        self.__name = name

    def set_name_teacher(self, name):
        self.__name = name

    def get_name_teacher(self):
        return self.__name


class Student:
    def __init__(self, name):
        self.__name = name
        self.__grade_list = []

    def set_name_student(self, name):
        self.__name = name

    def get_name_student(self):
        return self.__name
    
    def set_grade_student(self, grade: int):
        self.__grade_list.append(grade)
    
    def get_avrg(self):
        if len(self.__grade_list) > 0:
            return sum(self.__grade_list) / len(self.__grade_list)
        return 0  


class Subject:
    def __init__(self, name, teacher: Teacher):
        self.name = name
        self.teacher = teacher  
        self.students_list = []  

    def add_student(self, student: Student):
        self.students_list.append(student)

    def grading(self):
        for student in self.students_list:
           
            grade = int(input(f"Please input grade of {student.get_name_student()} for subject {self.name}: "))
            student.set_grade_student(grade)
    
    def show_students_info(self):
        
        student_list_in_subject = sorted(self.students_list, key=lambda student: student.get_avrg(), reverse=True)
        
        for student in student_list_in_subject:
            print(f"{student.get_name_student()}: {student.get_avrg()}")


# Testing the functionality
teacher = Teacher("ali")
subject = Subject("Math", teacher)

# Adding students
student1 = Student("reza")
student2 = Student("amir")
subject.add_student(student1)
subject.add_student(student2)

# Grading students
subject.grading()

# Showing student info sorted by average grade
subject.show_students_info()
