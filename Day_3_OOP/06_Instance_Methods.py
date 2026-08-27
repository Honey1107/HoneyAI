# 06_Instance_Methods
class Student:

    # Class Variable
    school = "ABC School"

    # Constructor
    def __init__(self, name, age):
        # Instance Variables
        self.name = name
        self.age = age

    # Instance Method
    def display(self):
        print(self.name)
        print(self.age)
        print(self.school)

    # Class Method
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


# Objects
s1 = Student("Jaya", 25)
s2 = Student("Rahul", 22)

# Instance variables
print(s1.name)       # Jaya
print(s2.name)       # Rahul

# Class variable
print(Student.school)  # ABC School

# Instance method
s1.display()

# Class method
Student.change_school("XYZ School")