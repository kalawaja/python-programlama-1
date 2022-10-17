
import turkceKarakter as tr

parola = input("Parola giriniz: ")

try:
    tr.kontrol(parola)
except Exception as hata:
    print("Hata->", hata)

