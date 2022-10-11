
"""In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. 

(Türkçesi: Nesne Yönelimli Programlama, Python'da nesne tabanlı programlama yapmak için sınıflar ve nesneler kullanılır. Kalıtım, polimorfizm, kapsülleme gibi gerçek dünya öğelerini programlama yapmak için kullanılır.)"""

# Fakülte Programı -> her bir fakülte class içinde oluşturulsun

# Fakülte -> Bölüm -> Ders -> Öğrenci

class Egitim:
    bolum = "Bilgisayar Mühendisliği"
    kampus = "Bahcelievler"
    dekan = "Ahmet Yesevi"

class Veterinerlik:
    bolum = "Hayvan Bakımı"
    kampus = "Avcılar"
    dekan = "Mehmet Can"

fakulte1 = Egitim()       # Egitim sınıfından fakulte1 sınıfı oluşturuldu
print(type(fakulte1))
print(fakulte1.bolum, fakulte1.kampus, fakulte1.dekan)

fakulte2 = Veterinerlik() # Veterinerlik sınıfından fakulte2 sınıfı oluşturuldu
print(type(fakulte2))
print(fakulte2.bolum, fakulte2.kampus, fakulte2.dekan)