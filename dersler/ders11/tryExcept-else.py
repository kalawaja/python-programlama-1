
try:
    # hatalı olması olası kod bloğu yazılır
    s1 = int(input("Sayı giriniz: "))
    s2 = int(input("Sayı giriniz: "))
    bolum = s1 / s2

except Exception as hata:
    # hata sonucu ne yazdırırsın
    print("Değerler hatalıdır", hata)

else:
    bolum = s1 / s2
    print("Bölüm: ", int(bolum))
    print("Hata oluşmadı")

finally:
    print("Bu blok her durumda çalışır.")