# contoh membuat exception

from numbers import Number

def tambah(a,b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise TypeError("input harus angka")
    return a + b

# print(tambah(7, "suki"))   # <-- ini akan error
print(tambah(9, 9.7))        # <-- ini akan lancar


# comtoh lain
print("\n","="*10,"PROGRAM KE-2", "="*10, "\n")

# angka = int(input("masukkan angkanya: "))
# try:
#     hasil = 7/angka
#     print(hasil)
# except Exception as error_message:
#     print(error_message)


while True:
    try:
        angka = float (input("masukkan angkanya: "))
        hasil = 777/angka
        if hasil.is_integer():
            print(int(hasil))
        else:
            print(hasil)
    except ZeroDivisionError as error_message:
        print(error_message)
    except ValueError:
        print("hanya boleh angka")
    
    pilihan = input("apakah kamu ingin mengulang programnya: y/n\n").lower()
    if pilihan == "n":
        print("program telah di hentikan")
        break
    elif pilihan == "y":
        continue
    else:
        print("apalah SUKI")
        break