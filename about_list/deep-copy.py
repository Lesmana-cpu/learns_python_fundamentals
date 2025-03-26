# catatan :
# kalo ingin nge copy list nested (bersarang), make deepcopy. karena kalo make copy biasa list yang ada di dalem listnya addresnya bakalan sama

data_1 = [1,2]
data_2 = [3,4,5]

data_2D = [data_1, data_2, 7]
data_2D_copy = data_2D.copy()

print(f'data = {data_2D}')
print(f'data = {data_2D_copy}')

# mengambil data dari nested list
data = data_2D[1][0]
print(data)

# address semuanya
print(f'address asli = {hex(id(data_2D))}')
print(f'address asli = {hex(id(data_2D_copy))}\n')


print('addres asli dari member')
print(f'address asli = {hex(id(data_2D[0]))}')
print(f'address copy = {hex(id(data_2D_copy[0]))}\n')


# makai deepcopy

from copy import deepcopy as dp
data_2D
data_2D_deepcopy = dp(data_2D)
print(f'address asli = {hex(id(data_2D))}')
print(f'address asli = {hex(id(data_2D_deepcopy))}\n')

print('addres asli dari member ke-1')
print(f'address asli = {hex(id(data_2D[0]))}')
print(f'address deepcopy = {hex(id(data_2D_deepcopy[0]))}')


data_2D[1][2] = 99
print(f'data asli = {data_2D}')
print(f'data copy = {data_2D_copy}')
print(f'data deepcopy = {data_2D_deepcopy}')
