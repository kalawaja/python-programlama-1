
# Bir ürün aldınız ve ürünün yaşını (gün cinsinden) bulmak istiyorsunuz.
# 1. Fonksiyonun içinde datetime modülünü kullanarak ürünün yaşını bulunuz.
# 2. Kullanıcı ürünün alındığını tarihi (Yıl, Ay, Gün) girecek.
# 3. Ürünün yaşı gün cinsinden ekrana yazdırılacak.

def gunHesapla(yil, ay, gun):
    from datetime import datetime as dt
    simdi = dt.now()
    yas = simdi - dt(yil, ay, gun)
    return yas.days

yil = int(input("Ürünün Alındığı Yıl: "))
ay = int(input("Ürünün Alındığı Ay: "))
gun = int(input("Ürünün Alındığı Gün: "))

print("Satın Alınan Ürün: ", gunHesapla(yil, ay, gun), "gündür kullanılıyor.")