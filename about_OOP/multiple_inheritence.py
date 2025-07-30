class Anomali:
    def anomali(self,anml):
        self.anml = anml
        print(f"ini anomali {self.anml}")
        
class Hero:
    def hero(self,hero):
        self.hero = hero
        print(f"ini hero {self.hero}")
        
class mix(Anomali,Hero):
    pass 


asep = mix()

asep.anomali("asep")
asep.hero("jamal")       
