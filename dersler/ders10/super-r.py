
# python class yapısında input() kullanarak super() fonksiyonunu kullanımı

class Calisan:
    def __init__(self):
        pass
    
    def kisisel(self):
        adSoyad = input("Ad ve Soyadınız: ")
        telefon = input("Telefon Numaranız: ")
        eposta = input("E-Posta Adresiniz: ")
        print(adSoyad, telefon, eposta)
        
    def isTecrubesi(self):
        adet = int(input("Kaç İş Tecrubeniz Var: "))
        for isler in range(adet):
            kurum = input("Kurum Adı Giriniz: ")
            giris = input("İşe Giriş Tarihiniz: ")
            ayrilis = input("Ayrılıs Tarihiniz: ")
    
    def ogrDurumu(self):
        ogrenim = input("Öğrenim Durumunuz Nedir? ")
        
class Yonetici(Calisan):
    def __init__(self):
        super().__init__()  
    
    def bilgiler(self):
        self.kisisel()
        maas = int(input("Maaş Bilgilerini Giriniz: "))
        adres = input("Adres Bilgilerini Giriniz: ")
        print(maas, adres)
    def yaziliKaynaklar(self):
        kaynakTuru = input("Kaynak Türünü Gir: ")
        yayimevi = input("Yayınevi Gir: ")
        print(kaynakTuru, yayimevi)

calisan = Calisan()
yonetici = Yonetici()

print(calisan.kisisel())
print(yonetici.bilgiler())