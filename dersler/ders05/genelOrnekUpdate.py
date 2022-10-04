
import random, string

harf = string.ascii_lowercase 
adet = int(input("Kac Öğrenci Girilecek: "))

ogrenci = {} 

for idno in range(adet):
    sayi = random.randint(100, 999)
    ozel = random.choice(string.punctuation)
    karakter = random.choice(harf)

    adisoyadi = input("Öğrenci Adı Soyadı Girin: ")
    bolumu = input("Öğrenci Bölümü Girin: ")
    yas = int(input("Öğrenci Yaşı Girin: "))
    ogrID = (str(sayi)+ozel+karakter+str(yas))

    ogrenci.update({
        ogrID,
            {
                "adisoyadi" : adisoyadi,
                "bolumu" : bolumu,
                "yas" : yas
            }  
    })

print(ogrenci)

ogr_arama = input("Aramak istediğiniz öğrenci ID'sini girin: ")

arama = ogrenci(ogr_arama)
try:
    print(
        """ -- {} ID'li Öğrencinin --
        Adı Soyadı: {}
        Bölümü: {}
        Yaşı: {}""".format(ogr_arama, arama["adisoyadi"], arama["bolumu"], arama["yas"])
    )

except Exception as hata:
    print("Böyle bir öğrenci bulunamadı! Hata: ", hata)