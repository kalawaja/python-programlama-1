
# girilen yılın artık yıl olma durumunu kontrol eden python programı

# yıl 400'e bölünecek veya 4'e bölünüp 100'e bölünmeyecek

print("Bir yıl giriniz: ")
yil = int(input())

if yil % 4 == 0 and yil % 100 != 0:
    print("\nBu bir artık yıl")
elif yil % 400 == 0:
    print("\nArtık yıl değil")
else:
    print("\nArtık yıl değil")

'''
yil = int(input("Yıl Girin: "))

if(yil % 400 == 0 or (yil % 4 == 0 and yil % 100 != 0)):

'''