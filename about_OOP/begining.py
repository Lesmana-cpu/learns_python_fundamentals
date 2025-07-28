class Hero:  # <-- template
    pass


hero1 = Hero() # <-- object / instance
hero2 = Hero()

hero1.name = "Superman"
hero1.health = 100
hero1.age = 30

hero2.name = "Haya"
hero2.health = 99
hero2.age = 25

print(hero1)
print(hero1.__dict__) # <-- menampilakan atribut dari objek
print(hero2.name) # <-- mengambil nama dari objek