
####### String Formatlama ########
print(" String Formatlama ".center(30,"-"))

# Sistem Dosyalarını Projemde Kullanmak için os modülünü dahil ediyorum
import os

adSoyad = input("Adınız ve Soyadınız: ")
brans = input("Branşınız: ")
maas = int(input("Maaşınız: "))

os.system("clear") # Terminal Temizleme Komutu
print("""Adınız.: {}
Branş: {}      
Maaş..: {}""".format(adSoyad, brans, maas))
