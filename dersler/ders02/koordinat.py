
# Koordinat Düzlemi Bölgesi Hesaplayan Python Programı

xKoor = int(input("Sayısal Değer Girin: "))
yKoor = int(input("Sayısal Değer Girin: "))

if (xKoor == 0 and yKoor == 0):
    print("Başlangıç Noktasındasın")
else:
    if (xKoor > 0):
        if (yKoor > 0):
            print("1. Bölgedesin", xKoor, yKoor)
        else:
            print("4. Bölgedesin", xKoor, yKoor)
    else:
        # x'in negatif olduğu yerler
        if (yKoor > 0):
            print("2. Bölgedesin", xKoor, yKoor)
        else:
            print("3. Bölgedesin", xKoor, yKoor)
