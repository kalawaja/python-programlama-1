
class Egitim:
    bolum = "Bilgisayar Mühendisliği"
    kampus = "Bahcelievler"
    dekan = "Ahmet Yesevi"

    def bolumDegistir(self):
        self.bolum = input("Fakülte 1 için; Yeni Bölüm Adı Giriniz: ")
        return self.bolum

class Veterinerlik:
    bolum = "Hayvan Bakımı"
    kampus = "Avcılar"
    dekan = "Mehmet Can"

    def bolumDegistir(self):
        self.bolum = input("Fakülte 2 için; Yeni Bölüm Adı Giriniz: ")
        return self.bolum

fakulte1 = Egitim()      # Egitim sınıfından fakulte1 sınıfı oluşturuldu
print(type(fakulte1.bolum))

print(fakulte1.bolumDegistir())

fakulte2 = Veterinerlik() # Veterinerlik sınıfından fakulte2 sınıfı oluşturuldu
print(type(fakulte2.bolum))

print(fakulte2.bolumDegistir())