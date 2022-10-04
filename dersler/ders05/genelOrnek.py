
import random, string

harf = string.ascii_lowercase # ascii_lowercase harfleri alır (küçük harflerden oluşan bir değişkene atadık)

adet = int(input("Kac Öğrenci Girilecek: "))

liste = [] # sonradan sözlüğe atamak için boş bir liste oluşturduk

for idno in range(adet):
    sayi = random.randint(1000, 9999) # 3 basamaklı rastgele sayı üretir
    ozel = random.choice(string.punctuation) # özel karakteri rastgele oluşturur
    karakter = random.choice(harf) # harf dizisinden bir karakteri rastgele oluşturur

    ogrID = (str(sayi)+ozel+karakter)
    liste.append(ogrID) # liste içine atadık

print(liste)

"""import random, string

harf = string.ascii_lowercase # ascii_lowercase harfleri alır (küçük harflerden oluşan bir değişkene atadık)
adet = int(input("Kac Öğrenci Girilecek: "))

ogrenci = {} 

for idno in range(adet):
    sayi = random.randint(100, 999) # 3 basamaklı rastgele sayı üretir
    ozel = random.choice(string.punctuation) # özel karakteri rastgele oluşturur
    karakter = random.choice(harf) # harf dizisinden bir karakteri rastgele oluşturur

    ogrenci["ogrID"] = (str(sayi)+ozel+karakter)
    # liste.append(ogrID) 
    ogrenci["adisoyadi"] = input("Öğrenci Adı Soyadı Girin: ")
    ogrenci["bolumu"] = input("Öğrenci Bölümü Girin: ")
    ogrenci["yas"] = input(input("Öğrenci Yaşı Girin: "))
    print(ogrenci)"""



