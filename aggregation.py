class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f'Student : {self.name}')

class Departement:
    def __init__(self, student):
        self.student = student

    def show_student(self):
        self.student.display()

student = Student("Sandhya")

department = Departement(student)


del student
department.show_student()  # it is exist 
student.display()          #name 'student' is not defined