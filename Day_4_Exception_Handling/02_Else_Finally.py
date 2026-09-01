# 02_Else_Finally
try:
    number = int("100")
except ValueError:
    print("Invalid")
else:
    print(f"Valid number: {number}")
