class Hero:
    
    # privat class variable
    __jumlah = 0
    
    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor
        self.__level = 1
        self.__experince = 0
        
        self.__healthMax = self.__healthBase * self.__level
        self.__attackPower = self.__attPowerBase * 0.7 * self.__level
        self.__armor = self.__armorBase * 0.3 * self.__level
        
        self.__health = self.__healthMax
        Hero.__jumlah += 1
        
    @property
    def info(self):
        return f"\nName = {self.__name}\nlevel = {self.__level}\nHealthBase = {self.__healthBase}\nhealth(Max) = {self.__health}\nattack power = {self.__attackPower}\narmor = {self.__armor}"
    
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self,addExp):
        self.__experince = addExp
        if(self.__experince >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__experince -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attackPower = self.__attPowerBase * 0.7 * self.__level
            self.__armor = self.__armorBase * 0.3 * self.__level
            
    def attack(self,musuh):
        self.gainExp = 50
        
        
suki = Hero("suki",100,25,70)
print(suki.info)

suki.gainExp = 50
suki.gainExp = 120
print(suki.info)
                
        
        