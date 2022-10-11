
# Python class yapısında super() fonksiyonu, bir sınıfın başka bir sınıfı miras almasını sağlar.

class Calisan:
    def __init__(self, adSoyad, telefon, maas):
        self.adSoyad = adSoyad
        self.telefon = telefon
        self.maas = maas
        # email adresi için; adSoyad değişkenini küçük harf yap ve boşluğu kaldırarark email adresi oluştur
        self.email = adSoyad.lower().replace(" ", "") + "@hotmail.com"

    def bilgileriGoster(self):
        print("""Ad Soyad: {}
Telefon: {}
Maaş: {}
Email: {}""".format(self.adSoyad, self.telefon, self.maas, self.email))

class Yonetici(Calisan):
    def __init__(self, adSoyad, telefon, maas, kisiSayisi):
        super().__init__(adSoyad, telefon, maas)
        self.kisiSayisi = kisiSayisi

yonetici1 = Yonetici("Ramazan Ilter", "+901234567890", 5000, 10)
yonetici1.bilgileriGoster()