
sayi1 = int(input("Birinci Sayi: "))
sayi2 = int(input("İkinci Sayi: "))
print("Sayılar Toplamı: ", sayi1+sayi2)

print(f""" -- ARİTMETİKSEL İŞLEMLER -- 
    Sayılar Toplamı: {sayi1 + sayi2}
    Sayılar Farkı  : {sayi1 - sayi2}
    Çarpımı        : {sayi1 * sayi2}
    Bölümü         : {sayi1 / sayi2}
    Karesi         : {sayi1 ** sayi2}
    Kalanı         : {sayi1 % sayi2}
    Tam Bölümü     : {sayi1 // sayi2}""")

print()

print(f""" -- ARİTMETİKSEL İŞLEMLER -- 
    Sayılar Toplamı: {sayi1 + sayi2}
    Sayılar Farkı  : {sayi1 - sayi2}
    Çarpımı        : {sayi1 * sayi2}
    Bölümü         : {round(sayi1 / sayi2, 3)}
    Karesi         : {sayi1 ** sayi2}
    Kalanı         : {sayi1 % sayi2}
    Tam Bölümü     : {sayi1 // sayi2}""")