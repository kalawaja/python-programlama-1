
# 1-10 arası sayıları terminale yazdıran program

sayac = 0

while sayac < 10:
    sayac = sayac + 1
    print(sayac)

""" # Arasındaki fark önemli
sayac = 0

while sayac < 10:
    print(sayac)
    sayac = sayac + 1
"""

# sep operatörü
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep="*")

# end operatörü
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, end="*")


# q tuşuna basıldığında programı sonlandıran python programı
from time import sleep

metin = ""
while True: # (metin != "q") or (metin != "Q") -> bu da yazılabilir
    if(metin == "q" or (metin == "Q")):
        print("Program sonlandırılıyor...")
        sleep(1)
        break
    metin = input("Herhangi bir şey yazın: ")
    print(metin)
