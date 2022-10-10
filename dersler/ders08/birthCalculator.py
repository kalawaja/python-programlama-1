
def yasHesapla(y):
    from datetime import datetime as dt
    simdi = dt.now()
    yas = simdi.year - y
    return yas

yil = int(input("Doğum yılınızı giriniz: "))
print("Yaşınız: ", yasHesapla(yil))

"""def yasHesapla(yil):
    return 2022 - yil

def main():
    print("Dogum yilinizi giriniz: ")
    yil = int(input())
    print("Yasiniz: ", yasHesapla(yil))

if __name__ == "__main__":
    main()"""