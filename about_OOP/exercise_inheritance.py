class Anomali:
    
    def __init__(self, name):
        self.__name = name
        self.__exp = 0
        self.__level = 0
        
        # pool default
        self.__health_pool = [17,27,37,47,57,67,77,87,97,100]
        self.__attPower_pool = [7,17,27,37,47,57,67,77,87,97]
        self.__armor_pool = [3,5,7,9,10,11,17]
        
        # default stats
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[min(self.__level, len(self.__armor_pool)-1)]
        
    def show_info(self):
        print("Name: {}\nLevel: {}\n\tHealth: {}\n\tAttack Power: {}\n\tArmor: {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.__attPower,
            self.__armor
        ))

    # Getter & Setter Pool
    @property
    def health_pool(self):
        return self.__health_pool

    @health_pool.setter
    def health_pool(self, input_health):
        self.__health_pool = input_health

    @property
    def attPower_pool(self):
        return self.__attPower_pool

    @attPower_pool.setter
    def attPower_pool(self, input_attPower):
        self.__attPower_pool = input_attPower

    @property
    def armor_pool(self):
        return self.__armor_pool

    @armor_pool.setter
    def armor_pool(self, input_armor):
        self.__armor_pool = input_armor

    def gain_exp(self, amount):
        self.__exp += amount
        if self.__exp >= 100:
            naik = self.__exp // 100
            self.__exp %= 100
            self.level_up(naik)

    def level_up(self, jumlah=1):
        self.__level += jumlah
        # Pastikan level tidak melebihi indeks pool
        max_health_idx = min(self.__level, len(self.__health_pool)-1)
        max_att_idx = min(self.__level, len(self.__attPower_pool)-1)
        max_armor_idx = min(self.__level, len(self.__armor_pool)-1)

        self.__health = self.__health_pool[max_health_idx]
        self.__attPower = self.__attPower_pool[max_att_idx]
        self.__armor = self.__armor_pool[max_armor_idx]

class anml_intelligent(Anomali):
    
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,57,107,157,207,257]
        self.attPower_pool = [0,27,37,47,57,67]
        self.armor_pool = [0,1.5,2.5,3.5,4.5,5]
        self.level_up(1)

class anml_strength(Anomali):
    
    def __init__(self,name):
        super().__init__(name)   
        self.health_pool = [0,150,170,190,240,290]
        self.attPower_pool = [0,20,30,40,50,60]
        self.armor_pool = [0,2,4,6,8,10]
        self.level_up(1)

djarkoni = anml_intelligent("Djarkoni")
dark_sep = anml_strength("Dark sepat")

djarkoni.show_info()
dark_sep.show_info()
