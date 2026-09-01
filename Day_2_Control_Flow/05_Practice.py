# 05_Practice
students = [
    {"name": "Alice", "marks": 95},
    {"name": "Bob", "marks": 72},
    {"name": "Charlie", "marks": 58}
]


def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


for student in students:
    grade = calculate_grade(student["marks"])
    print(f"{student['name']} -> {student['marks']} -> Grade: {grade}")
