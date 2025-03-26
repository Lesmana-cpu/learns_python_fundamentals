data = ['hai', 'asep', 'mewing', 'L7']

data.insert(1, 'berak')  # data.insert(indexnya, data yang di tambahkan)
print(f'{data}  <-- ini data.insert') 

data.append('wtf')  #data.append <-- menambahkan data paling akhir
print(f'{data} <-- ini data.append')

len_data = len(data)
print(f'{len_data} <-- panjang data')

data_behind = data[-1]
print(f'{data_behind} <-- data paling belakang\n')


# add list with list
penambahan_angka = [1, 2, 3, 4, 5, 3**2]
data.extend(penambahan_angka)
print(f'menambahkan list {penambahan_angka} ke list data, hasilnya = {data}\n')

# changes data
data[3] = 'Lesman'
print(f'merubah data dari yang tadinya index 3 itu = asep, sekarang index 3 itu = {data[3]}\n')

# removing data
data.remove('berak')
print(f'berak sudah di remove, jadi data sekarang adalah = {data}')

# removing data most behind
data_pop = data.pop()    # <-- pop adaalah data akhir yang di hapus
print(f'data akhir yang di hapus (pop) adalah = {data_pop}')

data.pop
print(f'data sekarang adalah = {data}')