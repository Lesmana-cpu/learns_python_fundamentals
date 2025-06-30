class anomali:
    
    def __init__(self,name,IQ,Strength):
        self.name = name
        self.IQ = IQ
        self.strength = Strength
        
    def showInfo(self):
        print("{} dengan IQ {} dan kekuatan {}".format(self.name,self.IQ,self.strength))
        
class anml_intelligent(anomali):
    def __init__(self, name):
        # anomali.__init__(self,name,700)
        super().__init__(name,300,150)   # <-- mengambil init dari super class
        super().showInfo()
        
class anml_strength(anomali):
    def __init__(self,name):
    #     self.name = name
    #     self.IQ = 200
         super().__init__(name,150,300)
         super().showInfo()

class gacor(anomali):
    def __init__(self,IQ,Strength):
        super().__init__("L7",IQ,Strength)
        super().showInfo()
        

asep = anml_intelligent("asep")
ujang = anml_strength("ujang")


print(asep.__dict__)
print(ujang.__dict__)

L7 = gacor(300,300)