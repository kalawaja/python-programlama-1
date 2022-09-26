
ad = input("Adınızı Girin: ") 
soyad = input("Soyadınızı Girin: ")
yas = int(input("Yaşınızı Girin: ")) # tip dönüşümü yaptık
maas = float(input("Maaşı Gir: "))

print(type(yas), "\t", type(maas), "\n", maas)
# \t → sekme işareti, \n → Bir alt satıra geçmek 
print(ad, "Aldığı Maaş:", round(maas), "₺")