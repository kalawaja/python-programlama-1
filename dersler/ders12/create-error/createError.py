
try:
    s1 = int(input("Birinci sayi.: "))
    s2 = int(input("İkinci  sayi.: "))
    bolum = s1 / s2
except Exception as hata:
    print("Hata →", hata)
    
    with open("hatali.txt", "a", encoding="utf-8") as hatakaydi:
        print(hata, file=hatakaydi)
else:
    with open("sonuc.txt", "a", encoding="utf-8") as sonuc:
        print("{}:{}={}".format(s1, s2, bolum), file=sonuc)