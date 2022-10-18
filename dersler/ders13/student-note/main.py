
# Kullanıcı adı ve parola bilgisi ilk başta dosyaya kaydolacak.
# Kullanıcı adı ve parola girildiğinde kullanıcı ve parola doğruysa hoşgeldiniz mesajı ve;
# Hatalı kullanıcı mesajı veren python programı:

# from notlar import *
import notlar

def kontrol(kullanici):
    import os   # ekran temizlemek için os modülü import edildi.
    bilgi = kullanici.split(" : ")
    # print(bilgi)
    while True:
        # Sisteme giriş için bilgileri istiyoruz. (Sign in)
        os.system("clear")    # ekran temizlendi.
        print("Kullanıcı Girişi".center(30, "#"))
        user = input("Kullanıcı adı: ")
        password = input("Parola: ")

        if user == bilgi[0] and password == bilgi[1]:
            os.system("clear")    # ekran temizlendi.
            print(f"Hoşgeldin {user}, Sisteme Giriş İzni Verildi. \n")
            notlar.menu()
            break
        else:
            print("Hatalı Giriş Yaptınız!")
            break
        
def main():
    userList = []
    # sisteme kullanıcı kaydı yapılıyor. (Sign up)
    with open("users.txt", "w", encoding="utf-8") as dosya:
        user = input("Kullanıcı adı: ")
        password = input("Parola: ")
        userList.append(dosya.write(user + " : " + password))

    with open("users.txt", encoding="utf-8") as dosya:
        for satir in dosya:
            kontrol(satir)

main()