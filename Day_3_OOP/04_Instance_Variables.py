# 04_Instance_Variables
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Jaya", 70000)
e2 = Employee("Rahul", 80000)

print(e1.salary)
print(e2.salary)
