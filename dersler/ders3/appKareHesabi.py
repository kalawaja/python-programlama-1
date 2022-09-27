
# girilen sayıya kadar olan sayıların karelerini ekrana yazdıran python programı

"""sayi = int(input("Sayı girin: "))
sayac = 0
from time import sleep
while sayac < sayi:
    sayac = sayac + 1
    sleep(1)
    print(sayac, "sayısının karesi", sayac ** 2, "dir.", end=" ")"""

# sayıların karelerini artırarak ekrana yazdıran python programı

sayi = int(input("Kaça kadar kare alınacak: "))
topla, basla = 0, 0

from time import sleep
while (basla < sayi):
    basla += 1
    sleep(1)
    kare = basla ** 2
    print(kare, end="->")
    topla += kare
    print(topla, "\n")


