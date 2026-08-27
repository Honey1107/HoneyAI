# 01_Classes
'''class Car:
    def start(self):
        print("Car started")


car = Car()
car.start()'''

'''class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


employee = Employee("Jaya", 70000)
employee.display()'''
'''
class Calculator:
    def add(self, a, b):
        return a + b


calculator = Calculator()
print(calculator.add(10, 20))'''
'''
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


student = Student("Jaya")
student.introduce()
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Jaya", 70000)
e2 = Employee("Rahul", 80000)

print(e1.salary)
print(e2.salary)
