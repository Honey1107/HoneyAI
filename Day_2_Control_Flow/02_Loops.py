# 02_Loops
# For Loop
for i in range(1, 6):
    print(i)

# While Loop
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

# Break
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue
for i in range(6):
    if i == 3:
        continue
    print(i)

# Pass
for i in range(3):
    pass
