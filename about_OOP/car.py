class car:
    jumlah = 0
    def __init__(sf,warna,ban,merk):
        sf.warna = warna
        sf.roda = ban
        sf.merk = merk
        car.jumlah += 1
        
mc = car("kuning",4,"mclaren")
bj = car("kuning",2,"bajai")

bj.roda = 3

print(mc.__dict__)
print(bj.__dict__)
print(car.jumlah)
