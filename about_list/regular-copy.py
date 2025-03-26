a = [1, 2, 7, 8, 3, 9, 11, 75]

b = a  # <--- ini addres nya sama
c = a.copy() # <-- ini addres nya beda

b.sort() # <-- aksi
c.reverse() # <-- aksi

print(a)
print(b)
print(f'{c}\n')

print(f'addres/memory a adalah : {hex(id(a))}')
print(f'addres/memory b adalah : {hex(id(b))}')
print(f'addres/memory c adalah : {hex(id(c))}')



