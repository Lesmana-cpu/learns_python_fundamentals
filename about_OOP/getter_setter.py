import os
os.system('cls' if os.name == 'nt' else 'clear')

class Hero:
    
    def __init__(self, name, health, element, armor):
        self.name = name
        self.__health = health
        self.__skill = element
        self.__armor = armor
        # self.__info = f"\nName: {self.name} \nHealth: {self.__health} \nSkill: {self.__skill} \nArmor: {self.__armor}\n"  <-- kalo make ini variable publiknya ga bisa diubah
        
    @property
    def info(self):
        # return self.__info  
        return f"\nName: {self.name} \nHealth: {self.__health} \nSkill: {self.__skill} \nArmor: {self.__armor}\n"
    
    @property
    def armor (self):
        pass
    #Getter
    @armor.getter
    def armor(self):
        return self.__armor
    #Setter
    @armor.setter
    def armor(self, input_armor):
        self.__armor = input_armor
    #Deleter
    @armor.deleter
    def armor(self):
        print("Armor deleted")
        self.__armor = "ga ada (udh di apus)"
        
                    
L7 = Hero("Less",100, "Fire", "Iron")

print(L7.__dict__)   
print(L7.info)  # Using the property to get the info

L7.name = "L7"
print(L7.info)

# getter for armor
print(L7.armor)

# setter for armor
L7.armor = "Diamond"
print(L7.armor)
print(f"\n{L7.__dict__}")

# deleter for armor
del L7.armor
print(f"\n{L7.__dict__}")