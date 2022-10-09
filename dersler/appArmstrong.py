
# Armstrong Sayı Python Programı (0-1000 Aralığı)

""""Tüm basamaklarındaki rakamların sayı değerlerinin küpleri toplamı, kendisine eşit olan sayılara Armstrong sayı denir." (Örneğin; 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153) Bu bilgilere göre aşağıdaki sayılardan hangisi bir Armstrong sayıdır?"""

def armstrong(sayi):
    """Armstrong sayı kontrolü"""
    toplam = 0
    for rakam in str(sayi):
        toplam += int(rakam) ** 3
    return toplam == sayi

def main():
    """Ana program"""
    for sayi in range(1000):
        if armstrong(sayi):
            print(sayi)

if __name__ == "__main__":
    main()