
with open("python-programlama-1/dersler/ders12/file-write/hello-istanbul.txt", "a", encoding="utf-8") as dosya:
   metin = input("Metin giriniz: ")
   yazi = dosya.writelines(metin)

with open("python-programlama-1/dersler/ders12/file-write/hello-istanbul.txt", "r", encoding="utf-8") as dosya:
   oku = dosya.read()
   print("Belge İçeriği: ", oku)