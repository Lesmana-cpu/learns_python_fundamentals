data_angka = [1, 4,5,7,8,5,7,7,7,3,2,1]
# penambahan_spasi = ' '.join(data_angka)  <-- ini method nya string
# print(penambahan_spasi)

# count data

jumlah_data_7 = data_angka.count(7)
print(f'jumah angka 7 = {jumlah_data_7}')

# mengambil posisi data (indexnya)

nama = ['lesmana', 'linux', 'kali linux', 'blackarch']

indexnya = nama.index('linux')
print(f'index dari {nama[1]} adalah = {indexnya} ')

# mengurutkan list

print(f'data angka = {data_angka} sebelum di sort\n')

nama.sort()
data_angka.sort()

print(f'ini data angka setelah di sort = {data_angka}')
print(f'ini data nama setelah di sort {nama}')

# kebalikannya sort

data_angka.reverse()  # <-- reverse ini ga akan ngaruh kalo di pake sebelum ada sort
nama.reverse()
print(f'\nini data angka setelah di reverse = {data_angka}')
print(f'ini data nama setelah di reverse = {nama}\n')

data_angka.extend(nama)
print(f'ini penambahan data angka dengan data, nama = ({nama})\nhasilnya = {data_angka} ')