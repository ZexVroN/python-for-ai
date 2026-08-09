# == FOR LOOP ==

# Start from 0-1-2-3-4
for i in range(5):
    print(i)

# Hello World 5x
for i in range(5):
    print(f"{i + 1}. Hello World")

# Start from 1-2-3-4-5
for i in range(1, 6):
    print(i)

# Start from 0-2-4-6-8
for i in range(0, 10, 2):
    print(i)

# P-y-t-h-o-n
name = "Python"
for i in name:
    print(i)

colors = ["Red", "Yellow", "Green"]
for i in colors:
    print(f"I like {i}")

# == WHILE LOOP ==

count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1

name = "Deni Septiawan"
count = 1
while count <= 5:
    print(f"My name is {name}")
    count = count + 1
