# 08_Static_Methods
class Employee:
    _next_id = 1000  # class attribute used as a shared counter

    def __init__(self, name, annual_salary):
        self.name = name
        self._annual_salary = annual_salary  # backing field for the property
        self.id = Employee._next_id
        Employee._next_id += 1

    @property
    def annual_salary(self):
        """Getter -- looks like attribute access, runs code underneath."""
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, value):
        """Setter -- validation runs every time someone assigns."""
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._annual_salary = value

    @property
    def monthly_salary(self):
        """Read-only computed property -- no setter defined."""
        return round(self._annual_salary / 12, 2)

    @classmethod
    def from_monthly(cls, name, monthly_salary):
        """Alternative constructor -- a very common classmethod use case."""
        return cls(name, monthly_salary * 12)

    @staticmethod
    def is_valid_salary(value):
        """Utility that doesn't need self or cls -- just grouped here logically."""
        return isinstance(value, (int, float)) and value >= 0


e1 = Employee("Diya", 1_200_000)
print(e1.id, e1.name, e1.annual_salary, e1.monthly_salary)

e1.annual_salary = 1_500_000   # uses the setter
print("Updated monthly salary:", e1.monthly_salary)

try:
    e1.annual_salary = -100
except ValueError as e:
    print("Error caught:", e)

e2 = Employee.from_monthly("Rohan", 50_000)
print(e2.id, e2.name, e2.annual_salary)

print(Employee.is_valid_salary(50000), Employee.is_valid_salary(-5))