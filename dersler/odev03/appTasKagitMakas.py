
# "Class" yapısı kullanarak, Taş-Kağıt-Makas oyunu tasarlayınız.

# 1. Oyunda; 
# 1.1. "Random modülü" ve;
# 1.2. "Listeleme (dizi)" işlemlerini kullanmanız daha kolay olacaktır. 

# 2. Detaylar: 
# 2.1. Daha önceden içinde taş kağıt makas içeren liste oluşturun. 
# 2.2. Oyun 3 setten ve her set 3 tekrardan oluşsun. 
# 2.3. İki tekrarı kazanan birinci seti ve üç setten en az iki seti kazanan oyunu kazanır.

import random

class Oyun:
    def __init__(self):
        self.oyun = ["taş", "kağıt", "makas"]
        self.oyuncu1 = 0
        self.oyuncu2 = 0

    def oyunuBaslat(self):
        for i in range(3):
            print("Set", i+1)
            for j in range(3):
                print("Oyun", j+1)
                oyuncu1_secim = input("Oyuncu 1 seçim: ")
                oyuncu2_secim = random.choice(self.oyun)
                print("Oyuncu 2 seçim:", oyuncu2_secim)
                if oyuncu1_secim == oyuncu2_secim:
                    print("Berabere")
                elif oyuncu1_secim == "taş" and oyuncu2_secim == "makas":
                    print("Oyuncu 1 kazandı")
                    self.oyuncu1 += 1
                elif oyuncu1_secim == "kağıt" and oyuncu2_secim == "taş":
                    print("Oyuncu 1 kazandı")
                    self.oyuncu1 += 1
                elif oyuncu1_secim == "makas" and oyuncu2_secim == "kağıt":
                    print("Oyuncu 1 kazandı")
                    self.oyuncu1 += 1
                else:
                    print("Oyuncu 2 kazandı")
                    self.oyuncu2 += 1

        if self.oyuncu1 > self.oyuncu2:
            print("Oyuncu 1 oyunu kazandı")
        elif self.oyuncu1 < self.oyuncu2:
            print("Oyuncu 2 oyunu kazandı")
        else:
            print("Oyun berabere")

oyun = Oyun()
oyun.oyunuBaslat()