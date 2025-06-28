class anomali:
    
    def __init__(self,name,IQ,strength):
        self.name = name
        self.IQ = IQ
        self.strength = strength
        
class anml_intelligent(anomali):
    pass

class anml_strength(anomali):
    pass

suki = anomali("suki",100,100)
L7 = anml_intelligent("L7",137,99)
man = anml_strength("man",101,157)

print(suki.__dict__)
print(L7.__dict__)
print(man.__dict__)