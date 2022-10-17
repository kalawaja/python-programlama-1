
# Try Except ile hata kontrolü

"""try:
    sayi1 = int(input("Sayı giriniz: "))
    sayi2 = int(input("Sayı giriniz: "))
    print(sayi1 / sayi2)
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz.")
except ValueError:
    print("Lütfen sadece sayı giriniz.")
except:
    print("Bir hata oluştu.")"""

try:
    # hatalı olması olası kod bloğu yazılır
    s1 = int(input("Sayı giriniz: "))
    s2 = int(input("Sayı giriniz: "))
    bolum = s1 / s2
    print("Bölüm: ", int(bolum))    # bölümü int'e çevirerek yazdırıyoruz

except Exception as hata:
    # hata sonucu ne yazdırırsın
    print("Değerler hatalıdır", hata)

finally:
    print("Bu blok her durumda çalışır.")