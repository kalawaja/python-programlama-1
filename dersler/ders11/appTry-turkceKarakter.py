
# Girilen şifrede Türkçe karakteri bulan ve listeleyen python programı

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

parola = input("Şifrenizi giriniz: ")

try:
    kontrol(parola)

except Exception as hata:
    print("Hata: ", hata)
    print("Türkçe karakterler: ", trListe)
