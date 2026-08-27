# 01_Try_Except
# ============================================================
# 1. try-except-else
# ============================================================

try:
    # Take input from the user and convert it to an integer
    number = int(input("Enter your number: "))

    # Print the entered number
    print(number)

except ValueError:
    # This block runs if the user enters something
    # that cannot be converted into an integer
    print("Invalid")

else:
    # This block runs only when NO exception occurs
    print(f"Valid number: {number}")


# ============================================================
# 2. try-except
# ============================================================

try:
    # Convert the string "100" into an integer
    number = int("100")

    # Print the converted number
    print(number)

except ValueError:
    # This block runs if conversion fails
    print("Invalid number")


# ============================================================
# 3. try-finally
# ============================================================

try:
    # Code that we want to execute
    print("Processing")

finally:
    # This block ALWAYS runs,
    # whether an exception occurs or not
    print("Cleanup")