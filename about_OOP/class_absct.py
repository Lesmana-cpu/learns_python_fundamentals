# class abstract
# abc = abstract base class
from abc import ABC, abstractclassmethod

class Button(ABC):
    
    @abstractclassmethod
    def click(self):
        # print("button click")
        pass

class PushButton(Button):
    
    def click(self):
        print('push button')
        
        
tombol1 = PushButton()

tombol1.click()
help(tombol1)

        
    

    
