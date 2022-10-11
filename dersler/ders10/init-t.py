
class Bilisim:
    liste = []
    def __init__(self, sinifAdi):
        while True:
            print(""" --- {} Sınıfa Hoşgeldiniz --- 
            1- Ekle
            2- Sil
            3- Güncelle
            4- Çıkış""".format(sinifAdi))
            secim = int(input("Seçiminiz: "))
            if secim == 1:
                self.ekle()
            elif secim == 2:
                self.sil()
            elif secim == 3:
                self.guncelle()
            else:
                self.cikis()

    def yazdir(self):
        for eleman in self.liste:
            print(eleman)

    def guncelle(self):
        pass

    def ekle(self):
        brans = input("Branş Giriniz: ")
        ogretmen = input("Öğretmen Giriniz: ")
        sinif = input("Sınıf Giriniz: ")
        self.liste.append(brans)
        self.liste.append(ogretmen)
        self.liste.append(sinif)
        print(self.liste)

    def sil(self):
        silBrans = input("Silmek istediğiniz branşı giriniz: ")
        if silBrans in self.liste:
                a = self.liste.index(silBrans)
                for i in range(3):
                    self.liste.pop(a)
                    
        print(self.liste)

sinifAdi = input("Sınıf Adı Giriniz: ")
bolum1 = Bilisim(sinifAdi)


# init ile iç içe 2 tane liste oluşturarak öğrenci bilgilerini yazdırma (ödev)):