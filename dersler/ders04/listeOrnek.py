
# aranan eleman listede var mı yok mu ona göre işlem yapan program
donanim = []
adet = int(input("Kaç Adet Donanım Girilecek.: "))
for sayi in range(1, adet+1):
    aygit  = input("Aygıtı Girin.: ")
    donanim.append(aygit)

arama = input("Aranan Donanım Aygıtını Giriniz.: ")

# aranacak eleman donanım içinde var mı varsakaçıncı sırada
if (arama in donanim):
    print(donanim.index(arama) +1)
else:
    print("Aranan Eleman Bulunamadı")

print(donanim) # normal sıralı
donanim.sort() # artan - azalan sıralama
print(donanim[::-1]) # tersine çevirir