
try:
    s1 = input("Birinci Sayı: ")
    s2 = input("İkinci Syaı: ")
    bolum = s1 / s2
except Exception as hata:
    print("Hata: ", hata)

    with open("python-programlama-1/dersler/ders12/create-error/hata.txt", "a", encoding="utf-8") as hatakaydi:
        print(hata, file=hatakaydi)
else:
    with open("python-programlama-1/dersler/ders12/create-error/sonuc.txt", "a", encoding="utf-8") as sonuc:
        print("{}:{}={}".format(s1, s2, bolum), file=sonuc)