
sozluk = {
    "ID": "J01",
    "Adi_Soyadi": "Ramazan ilter",
    "Yas": "32",
    "Meslek": "Bilisim"
}
print(sozluk)

print(sozluk.keys()) # keys değerlerini sozluk içinde gösteririz

print(sozluk.values()) # values değerlerini sozluk içinde gösteririz

print(sozluk.items()) # Bütün elemanları irtibatlı(gruplu) şekilde gösterir

print(sozluk["ID"]) # ID değerini sozluk içinde gösteririz

print(sozluk.get("ID")) # ID değerini sozluk içinde gösteririz

print(sozluk.get("sinif")) # verilen key sozluk içinde var mı kontrolu yapar

print(sozluk.get("sinif", "Deger Yoktur")) # verilen key sozluk içinde var mı kontrolü yapar

print(sozluk.get("yas", "hata")) #key değerleri harf duyarlılığı vardır

sozluk["ID"] = "J02" # ID değerini değiştiririz

sozluk["yas"] = 32 # sozluk içindeki yas değerini 32 olarak değiştiririz