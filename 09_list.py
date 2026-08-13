my_list = []
print(f"My list = {my_list}")


colors = ["Red", "Blue", "Green"]
for i in range(3):
    print(f"{i + 1}. {colors[0 + i]}")

# Mix
mixed = [1, "Dua", True, 7.2]
for i in range(4):
    print(f"{i + 1}. {mixed[0 + i]}")

fruits = ["Mango", "Banana", "Orange"]
fruits[0] = "Coconut"
for i in range(3):
    print(f"{i + 1}. {fruits[0 + i]}")

# Slicing
fruits = ["Mango", "Banana", "Orange"]
print(f"This is slicing = {fruits[0:2]}")  # From index-0 and stop before index-2

# List can be changed
fruits = ["Mango", "Banana", "Orange"]
fruits[1] = "Dragon"
print(f"Fruits = {fruits}")


# Add list
fruits = ["Mango", "Banana", "Orange"]
fruits.append("Kiwi")
print(f"Fruits after add = {fruits}")

# Remove list from value
fruits = ["Mango", "Banana", "Orange", "Peach", "Watermelon"]
fruits.remove("Banana")
print(f"Fruits after remove = {fruits}")
# Remove list from last
fruits.pop()
print(f"Fruits after remove last = {fruits}")
# Remove list from index
del fruits[1]
print(f"Fruits after remove index-1 = {fruits}")

# == Other Method ==

# len()
# Menghitung jumlah item di dalam list
numbers = [3, 1, 5, 3, 9]
print(len(numbers))


# count()
# Menghitung berapa banyak suatu nilai di dalam list
print(f"Berapa banyak nilai 3 di dalam list = {numbers.count(3)}")

# index()
# Mencari posisi tertentu berada pada index keberapa
print(f"Nilai 1 berada di index-{numbers.index(1)}")  # Tanpa duplikat
print(
    f"Nilai 3 berada di index-{numbers.index(3)}"
)  # Duplikat, hasil = nilai pertama kali ditemukan

total = len(numbers)
for i in range(total):
    print(f"{i + 1}. Numbers = {numbers[i]}")

print(f"List after sort = {numbers.sort()}")
