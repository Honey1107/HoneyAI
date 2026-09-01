# 05_Class_Variables
class Employee:
    company = "ABC Technologies"

    def __init__(self, name):
        self.name = name


e1 = Employee("Jaya")
e2 = Employee("Rahul")

print(e1.company)
print(e2.company)
