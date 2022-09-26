
adiniz = input("Adınızı Girin: ")

print(adiniz[0:5]) # sıfırıncı karakterden dördüncü karaktere kadar yazdır
print(adiniz[:5]) # (Aynı çıktıyı verir)
print(adiniz[2:5])
print(adiniz[::2])
print()

sayilar = ["0","1","2","3","4","5","6","7","8","9","10"] 
print(sayilar[::2]) # Liste halindeki sayılardan çift sayıları yazdırmak için

sayilar = "0,1,2,3,4,5,6,7,8,9,10"
ciftSayilar = sayilar.split(",")
print(ciftSayilar[::2]) # Metinsel ifadelerden Çift Sayıları Yazdırmak için

print(ciftSayilar[::2], "\t", ciftSayilar[1::2]) 
# ciftSayilar[baslangic:bitis:artisMiktari]