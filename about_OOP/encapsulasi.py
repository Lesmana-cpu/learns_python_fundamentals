import os
os.system("cls" if os.name == "nt" else "clear")

class Hero:
    
    def __init__ (self, name, health, power, armor):
        self.__name = name
        self.__health = health
        self.__power = power
        self.__armor = armor
        
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter
    def diserang(self, power_musuh):
        rasa_serangan = power_musuh / self.__armor
        self.__health -= rasa_serangan
        self.__health = max(0, self.__health)
        
   
# awal dari game
haya = Hero("Hayabusa", 2000, 500, 125)    

print(haya.__dict__)

# running game
# print(haya.__name)  <-- ini akan error karena __name adalah private variable
print(haya.getName())

print(haya.getHealth())
haya.diserang(1500)
print(haya.getHealth())