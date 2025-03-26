angka = [1, 2, 3]
print(angka)

nama = ['L7', 'Lesmana', 'Kaya', 'Handsome']
print(nama)

bolean = [True, False, False, True]
print(bolean)

# cara alternatif membuat list

lis = list(range(0, 15))
print(f'{lis} ini list dan range\n')

# membuat list with foor loop
list_for = [i**2 for i in range(0, 21, 3)]
print(list_for, "ini list for\n") 

# membuat list pake for if
list_for_if = [i for i in range(0,9) if i != 7]  # != kalo bukan sama dengan 7 nya aja yg ga di print, kalo == 7 nya aja yang di print
print(list_for_if, 'ini list for if\n')

list_for_if_genap = [i for i in range(0,9) if i%2 == 0]  # != kalo bukan sama dengan 7 nya aja yg ga di print, kalo == 7 nya aja yang di print
print(f'{list_for_if_genap} ini list for if genap\n')

list_for_if_ganjil = [i**2 for i in range(0,9) if i%2 != 0]
print(f'{list_for_if_ganjil} ini list for i ganjil')