class Hero:
    
    # class variable
    jumlah = 0
    __privateJumlah = 0  # private class variable
    
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
        # variable instance private
        self.__private = "ini private"
        
        # variable instance protected
        self._protected = "ini protected"
        
jenifer = Hero("Jennifer", 125)

print(jenifer.__dict__)
jenifer.name = "Rose"
print(jenifer.__dict__)
print("\n")

# private
jenifer.__private = "change testing"
print(jenifer.__dict__)
print(jenifer.__private)
print("\n")

# protected
jenifer._protected = "change proteksi"
print(jenifer.__dict__)
print(jenifer._protected)
print("\n")

print(Hero.__dict__)
print(Hero.__privateJumlah)
