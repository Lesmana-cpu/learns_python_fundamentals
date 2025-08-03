class Hero:
    def __init__(self,name,skill,umur):
        self.name = name
        self.skill = skill
        self.umur = umur
        
    def __repr__(self):
        return "Debug -> Hero: {} dengan skill {} dan umur {}".format(self.name,self.skill,self.umur)
    
    
    def __str__(self):
        return "Hero: {} dengan skill {} dan umur{}".format(self.name,self.skill,self.umur)
        
        
    def __add__(self,objek):
        return self.umur + objek.umur
    
    @property     # <-- kalo dictionary harus di tambahin @property dulu
    def __dict__(self):
        return "objek ini punya nama {}, skill {} dan umur {}".format(self.name, self.skill, self.umur)
    
    
    
    
first_hero = Hero("Asep", "fire", 17)
second_hero = Hero("Joni", "ice", 19)

print(repr(first_hero))
print(first_hero)

print(first_hero + second_hero)
print(second_hero.__dict__)