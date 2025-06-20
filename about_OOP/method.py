import os
os.system('cls' if os.name == 'nt' else 'clear')

class Hero:
    # class variable
    jumlah = 0
    
    def __init__(self, inputName, inputHealth, inputElement, inputArmor):
        # instance variables
        self.name = inputName
        self.health = inputHealth
        self.skill = inputElement
        self.armor = inputArmor
        Hero.jumlah += 1
        
    # void function, method tanpa return, tanpa argument
    def who(self):
        print(f"my name is {self.name}")
        
    # method with arguments but no return
    def healthUp(self, up):
        self.health += up
        
    # method with return
    def getHealth(self):
        return self.health
    

hero1 = Hero("Jack", 200, "", "earth")
hero2 = Hero("Rose", 150, "Ice", "Gold")
hero3 = Hero("L7", 200, "Fire", "Diamond")

print(hero2.__dict__)
print(hero3.__dict__)

hero1.who()
hero3.healthUp(77)

print(hero3.health)

print(hero3.getHealth())