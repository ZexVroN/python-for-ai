# Empty Dictionary
my_dict = {}

# Dictionary with data
person = {"name": "Deni Septiawan", "age": 26, "city": "Palembang"}

# == Accessing Values ==
person = {"Name": "Deni Septiawan", "Age": 26, "City": "Palembang"}

# GET VALUES BY
print(person["Name"])  # Deni Septiawan
print(person["Age"])  # 26
print(person["City"])  # Palembang

# SAVER WITH GET()
# print(person["Job"])  = KeyError because Job is nothing
print(person.get("Job"))  # None : No Error
print(person.get("Job", "Unknown"))  # Unknown


# == Changing Disctionaries ==

# ADD
person["Email"] = "denysptwn@gmail.com"  # Add new
person["Age"] = 27  # Update existing
print(person)

# REMOVE ITEMS
del person["Email"]  # Remove by key
print(person)

person.clear()
print(person)

# == Dictionary Methods ==

# GET KEYS - VALUES - ITEMS
print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(
    person.values()
)  # dict_values(['Deni Septiawan', 26, 'Palembang'])# Deni Septiawan, 26, Palembang
print(person.items())  # 'Name', 'Deni Septiawan'), ('Age', 26), ('City', 'Palembang'

# CHECK IF KEY EXISTS
if "Name" in person:
    print("True")
else:
    print("False")

# UPDATE MULTIPLE VALUES
person.update({"Age": 30, "Job": "Engineer"})
print(person)

# == Nested Disctionaries ==
Students = {
    "Deni": {"Age": 27, "Grade": "A"},
    "Lina": {"Age": 29, "Grade": "A"},
    "Dimi": {"Age": 29, "Grade": "B"},
}

print(Students)

print(Students["Deni"]["Grade"])
print(f"Deni Grade is {Students['Deni']['Grade']}")
