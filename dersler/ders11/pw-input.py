
# pwinput ile girilen şifrede Türkçe karakteri bulan ve listeleyen python programı

# Terminal -> python3 -m pip install pwinput            (for mac)
# Terminal -> python3 -m pip install --upgrade pip      (for mac)

from pwinput import pwinput as pw

trListe = list()

def kontrol(parola):
    trKarakter = "çÇİıÖöŞşÜü"

    for krktr in parola:
        if krktr in trKarakter:
            trListe.append(krktr)
    
    if len(trListe) > 0:
        raise TypeError("Şifrede Türkçe karakter bulunamaz.")
    else:
        print("Şifre kabul edildi.")

parola = pw("Şifrenizi giriniz: ")

try:
    kontrol(parola)

except Exception as hata:
    print("Hata: ", hata)
    print("Türkçe karakterler: ", trListe)