# 03_Constructors
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


student = Student("Jaya")
student.introduce()
