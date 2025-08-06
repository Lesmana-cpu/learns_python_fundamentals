# class abstract & decorator

from abc import ABC, abstractmethod


class Button(ABC):
    
    def __init__(self,set_link):
        self.link = set_link
    
    @abstractmethod
    def click(self):
        pass
    
    
    @property
    @abstractmethod
    def link(self):
        pass
    
    
    
class PushButton(Button):
    
    def click(self):
        print(f"Go To {self.link} ")
        
    @Button.link.setter
    def link(self,InputLink):
        self.__link = InputLink
        
    @link.getter                     # <-- ga usah make Button lagi, karena sudah ada di atas nya
    def link(self):
        return self.__link
    
                
        
tombol1 = PushButton("github.com/lesmanadarajat")

tombol1.click()
