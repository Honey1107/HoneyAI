# 04_Data_Structures
# ---------------------- LIST ----------------------

numbers = [10, 20, 30, 40]

numbers.append(50)
numbers.extend([60, 70])
numbers.insert(1, 15)
numbers.remove(30)
numbers.pop()
numbers.sort()
numbers.reverse()
numbers.copy()
numbers.count(20)
numbers.index(40)
len(numbers)
max(numbers)
min(numbers)
sum(numbers)

print(numbers)

for num in numbers:
    print(num)


# ---------------------- TUPLE ----------------------

colors = ("Red", "Green", "Blue", "Black")

print(colors.count("Red"))
print(colors.index("Blue"))
print(len(colors))
print(max(colors))
print(min(colors))

for color in colors:
    print(color)


# ---------------------- SET ----------------------

languages = {"Python", "Java", "C++"}

languages.add("Go")
languages.update(["Rust", "JavaScript"])
languages.remove("Java")
languages.discard("Swift")
languages.copy()

backend = {"Python", "Java"}
frontend = {"JavaScript", "React"}

print(backend.union(frontend))
print(backend.intersection(frontend))
print(backend.difference(frontend))
print(backend.symmetric_difference(frontend))

print(languages)


# ---------------------- DICTIONARY ----------------------

employee = {
    "id": 101,
    "name": "Jaya",
    "salary": 50000
}

print(employee.keys())
print(employee.values())
print(employee.items())

employee.get("name")
employee.update({"salary": 60000})
employee.setdefault("department", "AI")
employee.pop("salary")
employee.copy()

for key, value in employee.items():
    print(key, ":", value)

