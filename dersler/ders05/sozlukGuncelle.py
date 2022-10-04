
ogrenci = dict()

ogrID = input("Öğrenci ID Girin: ")
adiSoyadi = input("Öğrenci Adı Soyadı Girin: ")
yas = input("Öğrenci Yaşı Girin: ")
bolum = input("Öğrenci Bölümü Girin: ")

ogrenci.update({
    "ID": ogrID, 
    "Adı Soyadı": adiSoyadi, 
    "Yaşı": yas, 
    "Bölümü": bolum
})

print("\nGirilen Bilgiler Kaydedildi\n", ogrenci.values())

"""ogrenci = dict()

ogrID = input("Öğrenci ID Girin: ")
adiSoyadi = input("Öğrenci Adı Soyadı Girin: ")
yas = input("Öğrenci Yaşı Girin: ")
bolum = input("Öğrenci Bölümü Girin: ")

ogrenci.update({
    "ID": ogrID, 
    "Adi_Soyadi": adiSoyadi, 
    "Yas": yas, 
    "Bolumu": bolum
})

silinen = ogrenci.pop("id") # sozluk içindeki yas değerini sileriz
print("Ogrenci Silindi, Silinen ID\t: ", silinen)
print(ogrenci)
# print("\nGirilen Bilgiler Kaydedildi\n", ogrenci.values())
print(ogrenci.clear()) # sozluk içindeki tüm değerleri sileriz"""