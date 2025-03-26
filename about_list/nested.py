# list 2D atau nested list

# contoh penggunaan

orang_genius_1 = ["Lesmana", 16, "Laki-laki"]
orang_genius_3 = ['Einstein', 40, 'Laki-laki' ]
orang_genius_2 = ['Tesla', 30, 'Laki-laki']

data_orang_genius = [orang_genius_1, orang_genius_2, orang_genius_3]


print('='*10 + " DAFTAR ORANG GENIUS " +'='*10 + '\n')
for people in data_orang_genius:
    print(f'Nama = {people[0]}')
    print(f'umur = {people[1]}')
    print(f'gender = {people[2]}\n')
    
    
# dengan reference

copy = data_orang_genius.copy()
print(f'List copy adalah = {copy}\n')
orang_genius_2[0] = "newton"
print(f'List copy adalah = {copy}\n')
print(data_orang_genius)