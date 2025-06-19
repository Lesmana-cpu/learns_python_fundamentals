class Hero:
    # class variable
    jumlah = 0
    
    # insatnce variable
    def __init__(self, name, health, element, armor):
        self.name = name
        self.health = health
        self.skill = element
        self.armor = armor
        Hero.jumlah += 1
        print(f"Creating Hero: {name}, Total Heroes: {Hero.jumlah}")
        
        
hero1 = Hero("ucup", 200, "Fire", "Iron")
hero2 = Hero("Haya", 150, "Ice", "Gold")
hero3 = Hero("L7", 200, "ALL ELEMENTS", "Diamond")


# print(hero1.__dict__)  <-- show atribute hero1
# print(hero2.__dict__)
# print(hero3.__dict__)   
# print(Hero.__dict__)  # This will show the class attributes and methods

print(Hero.jumlah)