# parameter is a place who get the data
name = "A"


def function_without_parameter():
    print("Hallo")


def function_with_parameter(name):
    print(f"Hallo {name}")
    return name


function_without_parameter  # Hallo
function_with_parameter("Deni")  # Hallo Deni


# MULTIPLE PARAMETERS
def calculate_total(price, tax_rate, discount_rate):
    tax = price * tax_rate
    discount = price * discount_rate
    final_price = price + tax - discount
    print(f"Total : Rp{final_price}")


calculate_total(10000, 0.05, 0.5)  # PRICE = 10K | TAX = 5% | DISCOUNT = 50%


# KEYWORD ARGUMENTS
def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")


create_profile(city="Palembang", name="Deni", age=27)
