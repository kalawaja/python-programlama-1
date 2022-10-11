
class Egitim:
    bolum = ""
    kampus = ""
    dekan = ""

    def bolumDegistir(self):
        self.bolum = input("Yeni Bölüm Adı Giriniz: ")
        self.ogrSayisi = int(input("Öğrenci Sayısı Giriniz: "))
        return self.bolum

    def kampusDegistir(self):
        self.kampus = input("Yeni Kampus Adı Giriniz: ")
        return self.kampus

    def dekanDegistir(self):
        self.dekan = input("Yeni Dekan Adı Giriniz: ")
        return self.dekan

    def ogrSayisi(self):
        return self.ogrSayisi

fakulte1 = Egitim()      # Egitim sınıfından fakulte1 sınıfı oluşturuldu
print(type(fakulte1))
print(fakulte1.bolum, fakulte1.kampus, fakulte1.dekan)

# sınıf içinde tanımlanan metodları çağırma
print(fakulte1.bolumDegistir(), "\n", fakulte1.kampusDegistir(), "\n", fakulte1.dekanDegistir(), "\n", fakulte1.ogrSayisi)