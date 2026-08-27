# 08_Practice
# ============================================================
# File Handling - All File Modes in One Program
# ============================================================

# ------------------------------------------------------------
# 1. w - Write Mode
# ------------------------------------------------------------
# Creates the file if it doesn't exist.
# If the file already exists, its old content is replaced.

with open("data.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("File Handling\n")

print("1. Write completed")


# ------------------------------------------------------------
# 2. r - Read Mode
# ------------------------------------------------------------
# Reads the existing content of the file.

with open("data.txt", "r") as file:
    content = file.read()

print("\n2. Read Mode:")
print(content)


# ------------------------------------------------------------
# 3. a - Append Mode
# ------------------------------------------------------------
# Adds new content to the END of the existing file.
# Existing content is not deleted.

with open("data.txt", "a") as file:
    file.write("Learning AI Engineering\n")

print("3. Append completed")


# Read again to verify appended content
with open("data.txt", "r") as file:
    print("\nAfter Append:")
    print(file.read())


# ------------------------------------------------------------
# 4. x - Create Mode
# ------------------------------------------------------------
# Creates a NEW file.
# If the file already exists, FileExistsError occurs.

try:
    with open("new_file.txt", "x") as file:
        file.write("This is a new file.")

    print("4. New file created successfully")

except FileExistsError:
    print("4. File already exists")


# ------------------------------------------------------------
# 5. wb - Write Binary Mode
# ------------------------------------------------------------
# Used to write binary data such as images, PDFs, etc.

binary_data = b"Hello Binary Data"

with open("binary_data.bin", "wb") as file:
    file.write(binary_data)

print("5. Binary file written")


# ------------------------------------------------------------
# 6. rb - Read Binary Mode
# ------------------------------------------------------------
# Reads data from a binary file.

with open("binary_data.bin", "rb") as file:
    data = file.read()

print("\n6. Read Binary:")
print(data)