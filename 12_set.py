# Kumpulan data yang hanya menyimpan nilai unik

# == Membuat Set ==

# SET KOSONG
empty_set = set()
print(empty_set)

# SET DENGAN NILAI
numbers = {1, 2, 3, 4, 5}
print(numbers)

fruits = set(["Apple", "Banana", "Orange"])
print(fruits)

# Dari list (Menghapus Duplikat)
scores = [85, 90, 85, 92, 90]
print(scores)
unique_scores = set(scores)
print(unique_scores)

# == Operasi Dasar ==
colors = {"red", "blue"}
print(colors)

# TAMBAH NILAI
colors.add("green")
print(colors)

# HAPUS NILAI
colors.remove("blue")  # ERROR JIKA TIDAK DITEMUKAN
colors.discard("biru")  # TIDAK ERROR JIKA TIDAK DITEMUKAN

if "red" in colors:
    print("Ada")
else:
    print("Tidak ada")

# REMOVE DUPLIKAT (LIST - SET)
names = ["Deni", "Lina", "Socksies", "Chienda", "Mony", "Chienda"]
print(names)
unique_names = set(names)
print(unique_names)


colors = {"red", "blue", "green"}

if "red" in colors:
    print("Red is available")
