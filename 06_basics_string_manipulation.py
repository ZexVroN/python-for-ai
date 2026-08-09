first_name = "Deni"
last_name = "Septiawan"

# Using +
fullname = first_name + " " + last_name
print("Full name = ", fullname)

# Using f-Strings (Modern python way!)
greeting = f"Hello, {first_name}!"
print("Greeting = ", greeting)

age = 26
print(f"I'm {first_name} and I'm {age} years old!")

star = "*"
stars = star * 10  # "**********"

separator = "-" * 20  # "--------------------"

text = "Python Programming"

print(text.lower())  # "python programming"
print(text.upper())  # "PYTHON PROGRAMMING"
print(text.title())  # "Python Programming"

messy = "  hello world  "
print(messy.strip())  # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)  # True
print(message.startswith("I"))  # True
print(message.endswith("Python"))  # True

# Find position
print(message.find("Python"))  # 7 (first occurrence)
print(message.count("Python"))  # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"
