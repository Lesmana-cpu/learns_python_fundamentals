class Hero:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        
    def attack(self, musuh):
        print(self.name + ' attacking ' + musuh.name)
        musuh.defend(self, self.power)
        
    def defend(self, musuh, power_musuh):
        print(self.name + ' defending ' + musuh.name)
        rasa_serangan = power_musuh/self.armor
        print('rasa serangannya: ' + str(rasa_serangan))
        self.health -= rasa_serangan
        print(f'jadi health {self.name}: ' + str(self.health))
        
L7 = Hero("L7", 200, 177, 77)
suki = Hero("Suki", 150, 100, 50)

L7.attack(suki)
print('\n')
suki.attack(L7)