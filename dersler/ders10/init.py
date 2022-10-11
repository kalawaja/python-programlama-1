
# Initializing a class

"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)"""

print("""Name: {p1.name} \n Age: {p1.age}""".format(p1=p1))

class Bilisim:
    def __init__(self, brans, ogretmen, sinif):
        self.brans = brans
        self.ogretmen = ogretmen
        self.sinif = sinif

    def yazdir(self):
        print(self.brans, self.ogretmen, self.sinif)

class Muhasebe:
    pass

brans = input("Branş: ")
ogretmen = input("Öğretmen: ")
sinif = input("Sınıf: ")

bolum1 = Bilisim(brans, ogretmen, sinif)
bolum1.yazdir()