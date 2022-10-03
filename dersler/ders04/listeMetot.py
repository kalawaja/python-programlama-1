
"""appent
expent
insert

remove
pop
del

enumerate()
max(arg1, arg2)
min(arg1, arg2)"""

# Bilgisayar Donanım aygıtlarını bir listeye aktaran python programı



# for sayi in adet:
#     aygit = input(sayi,". Aygıt Girin: ")
#     print(aygit)

donanim = []  # normal metin olarak ekler
liste = []  # elemanları harf olarak ekler

adet = int(input("Kaç Adet Donanım Girilecek.: "))
for sayi in range(1, adet+1):
    aygit  = input("Aygıtı Girin.: ")
    donanim.append(aygit)
    liste.extend(aygit)

print(donanim)
print(liste)