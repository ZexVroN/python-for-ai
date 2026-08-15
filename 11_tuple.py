# Tuple mirip dengan list, tetapi tidak dapat diubah setelah dibuat. Tuple adalah urutan yang tidak dapat diubah (immutable).

# == Creating tuples ==

# EMPTY TUPLE
empty = ()
print(empty)

# TUPLE WITH ITEMS
point = (3, 5)
print(point[0])

colors = ("Red", "Black", "White")
print(colors[0])
print(colors[0:2])  # SLICING

# SINGLE TUPLE (NEED COMMA)
single = (26,)
print(single[0])

not_tuple = 62
print(not_tuple[0])  # ERROR KARENA BUKAN TUPLE

# WITHOUT PARENTHESES (implicit)
coordinat = 10, 20
print(coordinat)

# == Tuple unpacking ==
point = (3, 5)
x, y = point
print(x)
print(y)
x, y = y, x
print(x)
print(y)

number = (10, 20, 30)
a, b, c = number
print(a)
print(b)
print(c)

# TUPLE TIDAK BISA DIUBAH
point = (3, 5)
point[0] = 4
print(point[0])

# NAMUN ADA SATU CARA MERUBAH TUPLE (Merubah ke list dan merubah lagi ke Tuple)
point = (3, 5)
temp = list(point)
temp[0] = 4
print(temp)
point = tuple(temp)
print(point)
