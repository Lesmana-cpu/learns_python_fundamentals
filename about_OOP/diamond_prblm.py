class X:
    def show(self,name):
        self.name = name
        print(f"ini {self.name} from class X")
        
class A(X):
    # def show(self,name):
    #     self.name = name
    #     print(f"ini {self.name} from class A")
    pass
        
        
class B(X):
    def show(self,name):
        self.name = name
        print(f"ini {self.name} from class B")
        
class Z(A,B):
    pass


objek = Z()
objek.show("Asep")