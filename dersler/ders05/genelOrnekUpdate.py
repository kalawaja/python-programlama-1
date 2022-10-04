
import random, string

harf = string.ascii_lowercase # kucuk harflerden oluşan diziyi bir değişkene ata
adet = int(input("Kac Ogrenci Girilecek.: "))

ogrenci = {}  # sonradan sozluğe cevireceğiz

for idno in range(adet):
    sayi = random.randint(100, 999) # 3 basamaklı sayı rasgele oluştur
    ozel = random.choice(string.punctuation)  # ozel karakteri random oluştur
    karakter = random.choice(harf) # harf dizisinden bir karakter belirle
    
       
    adisoyadi = input("Adı ve Soyadı: ")
    bolumu = input("Bolumu.: ")
    yas = int(input("Yaş.: "))
    ogrID = (str(sayi)+ozel+karakter+str(yas))
    
    ogrenci.update({
        ogrID:
            {
                "adisoyadi": adisoyadi,
                "bolumu": bolumu,
                "yas": yas
            }
        })

print(ogrenci)

ogr_arama = input("Aranan ID Giriniz.: ")

arama = ogrenci[ogr_arama]
try:
    print(
    """ -- {} ID'li Öğrencinin --
    Adı Soyadı\t: {}
    Bölümü \t:{}
    Yaş \t:{}""".format(ogr_arama, arama["adisoyadi"], arama["bolumu"], arama["yas"])
    )
except Exception as hata:        
    print("Ogrenci Yok.:", hata)