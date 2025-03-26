# 1. ini akan ketimpa
with open("data_2.txt", mode="w", encoding="utf-8") as file:
    file.write("asep si ucep")
    
with open("data_2.txt", mode="w", encoding="utf-8") as file:
    file.write("suki si suk")
    
    
with open("data_2.txt", mode="w", encoding="utf-8") as file:
    file.write("over write")  # <-- menghapus yg di atas nya, dan menggantinya (over write)
    
    
# 2. mode append

with open("data_3.txt", mode="w", encoding="utf-8") as file:
    file.write("jajang\n")
    
with open("data_3.txt", mode="a", encoding="utf-8") as file:
    file.write("suki si suk")
    
    
# 3. mode r+
with open("data_4.txt", mode="w", encoding="utf-8") as file:
    file.write("ini adalah file ke 4\n")

with open("data_4.txt", mode="r+", encoding="utf-8") as files:
    files.write("baris-1 = Asep\n")
    files.write("baris-2 \n")
    files.write("baris-3 \n")
    
with open("data_4.txt", mode="r+", encoding="utf-8") as files:
    data = files.read()
    print(data)
    
with open("data_4.txt", mode="r+", encoding="utf-8") as files:
    files.write("baris-1 = suki\n")  # <-- ini akan menimpa baris-1 = Asep (sesuai dengan panjang karakternya)
    