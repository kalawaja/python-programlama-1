
sayi = int(input("Sayı Gir: "))

if sayi >=0:
    if(sayi % 2 == 0):
        print("Sayı Çifttir")
    elif(sayi % 2 != 0):
        print ("Sayı Tektir")
else:
    print("Negatif Sayılar")