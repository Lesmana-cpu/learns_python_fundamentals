class X:
    def show(self):
        print("this is show x")

class Y:
    def show(self):
        print("this is show y")

class Z(X,Y):  # <-- urutannya ada di sini Z(1,2):
    def show(self):
        print("this is show z")

objek = Z()
objek.show()
help(objek)