
import re 
trListe = list()

def kontrol(parola):
    trKarakter = "çÇİıÖöŞşÜü"
    
    for krktr in parola:
        if len(parola) < 8:
            raise ValueError("Parola en az 8 karakter olmalıdır.")
        elif krktr in trKarakter:
            trListe.append(krktr)
        elif not re.search("[a-z]", parola):
            raise Exception("Parola en az bir küçük harf içermelidir.")
        elif not re.search("[A-Z]", parola):
            raise Exception("Parola en az bir büyük harf içermelidir.")
        elif not re.search("[0-9]", parola):
            raise Exception("Parola en az bir rakam içermelidir.")
        elif not re.search("[_@$]", parola):
            raise Exception("Parola en az bir özel karakter içermelidir.")
        else:
            print("Parola geçerli.")
            break
    if len(trListe) > 0:
        raise TypeError("Parola Türkçe karakter içeremez.", trListe)
        