class Hero:
    
    # private variable
    __jumlah_hero = 0
    def __init__(self, inputNama):
        self.__nama = inputNama
        Hero.__jumlah_hero += 1
    
    # method ini hanya bisa untuk objek    
    def get_jumlah_1(self):
        return Hero.__jumlah_hero
    
    
    # method ini tidak bisa untuk objek, tapi bisa untuk class
    def get_jumlah_2():
        return Hero.__jumlah_hero
    
    
    # method statik (decolator) bisa untuk objek dan class
    @staticmethod
    def get_jumlah_3():
        return Hero.__jumlah_hero
    
    # method class (decolator) bisa untuk objek dan class
    @classmethod
    def get_jumlah_4(cls):
        return cls.__jumlah_hero
    
    
asep = Hero("Asep")
haya = Hero("Hayabusa")

# print(Hero.get_jumlah_1())  <-- ini akan error karena get_jumlah_Hero adalah method objek
print(Hero.get_jumlah_2())

print(Hero.get_jumlah_3())
print(haya.get_jumlah_3())

print(asep.get_jumlah_4())
print(Hero.get_jumlah_4())

gogo = Hero("Gogo")
    
