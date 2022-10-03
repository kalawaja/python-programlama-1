
# pop → siler ve silinen elemanı döndürür
# clear → kümeyi temizler 
# remove → eleman silme
# del → bir sınıf olarak kullanılır oluşturulan listeyi RAM den siler 

donanim = []
adet = int(input("Kaç Adet Donanım Girilecek.: "))
for sayi in range(1, adet+1):
    aygit  = input("Aygıtı Girin.: ")
    donanim.append(aygit)

silme = input("Silinecek Donanım Aygıtını Giriniz.: ")

# aranacak eleman donanım içinde var mı? varsa kaçıncı sırada?
if (silme in donanim):
    
    silindi = donanim.pop(donanim.index(silme))
    eklenecek = input("Aygıtı Girin.: ")
    donanim.append(eklenecek)
else:
    print("Aranan Eleman Bulunamadı")

print("Silinen Eleman ", silindi, "Yeni Liste\t:", donanim)