
"""
for sayac in range(baslangic, bitis, artis):
    islemler
"""

# Başlangıç ve Bitiş arasındaki sayıları ekrana yazdıran python programı

baslangic = int(input("Başlangıç değeri girin: "))
bitis = int(input("Bitiş değeri girin: "))

if baslangic > bitis:
    print("Başlangıç değeri bitiş değerinden büyük olamaz!")
    exit(0)
else:
    for i in range(baslangic, bitis+1):
        if i % 2 == 0:
            continue
        else:
            print(i, end=" ")
