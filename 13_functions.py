# Functions
"""
def : For make Python know we make functions
say_hello : the name of functions
() : the parameter place
"""


def say_hello():
    print("Hallo bangz")


say_hello()  # Hallo bangz

# FIRST EXCERCISE
"""
Make functions for this one and call it :
=== CONTACT MANAGER ===
1. Add Contact
2. Show Contact
3. Search Contact
4. Delete Contact
5. Exit
"""


def show_menu():
    print("=== CONTACT MANAGER ===")
    print("1. Add Contact")
    print("2. Show Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


show_menu()


# PARAMETER & ARGUMENT
def greet(name):  # (name) is a Parameter "The place who get the data"
    print(f"Hallo {name}")


greet("Deni")  # Hallo Deni (This is a Argument) "The place who send the data"


# Make say_goodbye with parameter
def say_goodbye(Name):
    print(f"Tscuss {Name}")


say_goodbye("Deni")  # Tschuss Deni


def check_weather(temperature):
    if temperature > 30:
        print("Its hot asf bruh!")
    else:
        print("Nice weather bruh")


temperature = int(input("Input temperature = "))
check_weather(temperature)

# RETURN VALUE
discount_rate = 0.15


def apply_discount(price):
    discount = price * discount_rate
    return price - discount


# IF YOU WANNA USE THAT VALUE AGAIN, SHOULD MAKE A NEW VARIABLE FOR SAVE THAT VALUE
final_price = apply_discount(10000)
print(final_price)

# IF YOU JUST WANNA SEE ONCE AND NO NEED TO USE THAT VALUE AGAIN, YOU CAN JUST PRINT
print(apply_discount(10000))
