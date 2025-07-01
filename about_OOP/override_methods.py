class anomali:
    
    def __init__(self,name,IQ,Strength):
        self.name = name
        self.IQ = IQ
        self.strength = Strength
        
    def showInfo(self):
        # print("Tipe : {}\n\tName: {} dengan IQ {} dan kekuatan {}".format(tipe,self.name,self.IQ,self.strength)) -> tambahin variable tipe di method nya
        print("show info di main class")
        print("{} dengan IQ {} dan kekuatan {}".format(self.name,self.IQ,self.strength))
        
class anml_intelligent(anomali):
    def __init__(self, name):
        super().__init__(name,300,150)
        
    def showInfo(self):
        # super().showInfo('intelligent')
        print("show info di sub class")
        print("Name: {} \n\tTipe: intelligent\n\tIQ: {}\n\tstrength: {}".format(
            self.name,
            self.IQ,
            self.strength
            
            )
              )
        
class anml_strength(anomali):
    def __init__(self,name):
         super().__init__(name,150,300)
         
         
         
kuka = anml_strength("kaku")
denifer = anml_intelligent("denifer")

denifer.showInfo()
print("\n")
kuka.showInfo()
         
