# 03_Functions
def add(a, b):
    return a + b


def greet(name="Guest"):
    return f"Hello {name}"


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(add(5, 8))
print(greet())
print(greet("Jaya"))
print(factorial(5))
