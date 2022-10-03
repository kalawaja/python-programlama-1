
# sleep fonksiyonunu kullanabilmek için
from time import sleep 

# ekranı temizlemek için
from os import system  

# liste tanımlaması yapıyoruz
donanim = [] 

def main(): # ana fonksiyonumuz 
    while True: # sonsuz döngü
        system("cls") # ekranı temizleme
        print(""" Liste İşlemleri 

        1-Ekle()
        2-sil()
        3-Güncelle
        4-Listele
        5-Çıkış """)
        
        secim = int(input("Seçiminiz.: "))
        if secim == 1:
            ekle()
        elif secim == 2:
            sil()
        elif secim == 3:
            guncelle()
        elif secim == 4:
            listele()
        elif secim == 5:
            cikis()
        elif (secim < 1) or (secim > 5):
            print("Hatalı Seçim Yaptınız")
        else:
            print("Listeden Seçim Yapınız.")
        
def ekle(): 
    system("cls") 
    print("Ekleme Menüsü")
    adet = int(input("Kaç Donanım Girilecek: "))
    for sayi in range(adet):
        eleman = input("Eleman Girin.: ")
        donanim.append(eleman)
    print("Elemanlar listeye Eklenmiştir")
    sleep(1)

def sil():       
    arama = input("Silinecek Eleman girin.: ")
    if (arama in donanim):
        silindi = donanim.pop(donanim.index(arama))
    print("Eleman Silinmiştir")
    sleep(2)
    
def guncelle():   
    arama = input("Güncellenecek Eleman girin.: ")
    if (arama in donanim):
        silindi = donanim.pop(donanim.index(arama))
        yeni = input("Eklenecek Elemanı Girin: ")
        donanim.append(yeni)
   
    print("Eleman güncellenmiştir")
    sleep(2)

def listele():
    system("cls")
    for eleman in donanim:
        print(eleman, end="\t")
    sleep(1)

def cikis():
    exit(0)
 
main()