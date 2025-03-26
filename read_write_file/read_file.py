# membaca file external

print(f"{3*'='} Membaca file txt {3*'='}")
file = open("data_r.txt", mode="r")

print(f"status read : {file.readable()}")   # <-- mengecek apakah file ini bisa di baca atau tidak
print(f"status write : {file.writable()}") # <-- mengecek apakah file ini bisa di tulis atau tidak

# print(file.read())   # <-- baca seluruh file

print(file.readline(),end="") # <-- read the first line     (, end="") <-- ini fungsinya menghapus "\n" yang udh bawaan
print(file.readline(),end="") # <-- read the second line    (, end="") <-- ini fungsinya menghapus "\n" yang udh bawaan
# print(file.readline())   # <-- read the third line
# print(file.readline())   # <-- read the fourth line

# print(file.readlines()) # <-- membaaca semua baris sebagai list


print(f"apakah file sudah di close : {file.closed}" )

file.close()
print(f"apakah file sudah di close : {file.closed}")



## salah satu teknik membuka file di python

print(f"{3*'='} Membaca file txt dengan with {3*'='}")

with open("data_r.txt", mode="r") as file:
    content = file.readline()
    lis = file.readlines()
    print(content, end="")
    print(lis)
    print(f"apakah file sudah di close : {file.closed}")
print(f"apakah file sudah di close : {file.closed}")