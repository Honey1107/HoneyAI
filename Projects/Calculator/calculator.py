num1 = float(input("Enter your number: "))
num2 = float(input("Enter your another number: "))

print("Select the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter the operation: ")

if operation == "1":
    print(num1 + num2)
elif operation == "2":
    print(num1 - num2)
elif operation == "3":
    print(num1 * num2)
elif operation == "4":
    print(num1 / num2)
else:
    print("Error: Invalid operation")
