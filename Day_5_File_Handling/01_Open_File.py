# 01_Open_File
# Create and write to a file
with open("students.txt", "w") as file:
    file.write("Jaya, AI Engineer\n")
    file.write("Rahul, Data Scientist\n")
    file.write("Priya, Python Developer\n")

print("File created successfully.")


# Read the file
with open("students.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)


# Append new data
with open("students.txt", "a") as file:
    file.write("Amit, ML Engineer\n")

print("New student added.")


# Read line by line
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())