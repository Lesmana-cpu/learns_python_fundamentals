# exception akan terjadi saat program erro saat runtime 

data_user_1 = int(input("masukkan angkanya: "))
data_user_2 = int(input("masukkan angka selaajutnya: "))

try:
    hasil = data_user_1/data_user_2
    print(hasil)
except:
    print(f"{data_user_1} tidak bisa di bagi dengan {data_user_2}")



# contoh dalam read & write

try:
    with open("data.txt", mode="r") as file:
        print(file.read())
        
except:
    print("file data.txt tidak di temukan, membuat file baru")
    with open("data.txt", mode="w", encoding="utf-8") as file:
        file.write("file baru ")
