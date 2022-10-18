
# Kullanıcı adı ve parola bilgisi ilk başta dosyaya kaydolucak.
# Kullanıcı adı ve parola girildiğinde kullanıcı ve parola doğruysa hoşgeldiniz mesajı ve 
# hatalı Kullanıcı mesajı veren python programı

# from notlar import *
import notlar 

def kontrol(kullanici):
    import os # ekran temizleme için os modülü dahil edilir  
    bilgi = kullanici.split(":")
    # print(bilgi)
    while True:
        # sisteme giriş için bilgileri istiyoruz LOG-IN
        os.system("clear")
        print(" Kullanıcı Girişi ".center(30,"#"))
        user = input("Kullanici Adi: ")
        password = input("Parola...: ")
        
        if (user == bilgi[0]):
            if (password == bilgi[1]):
                os.system("clear")
                print(f"Hoş Geldin {user}, Sisteme Giriş İzni Verildi \n")
                notlar.menu()
                break
            else:
                print("Hatalı Giriş")
                continue   
            
def main():
    userList = []
    # sisteme yeni kullanıcı kaydı yapılıyor SIGN-IN
    with open("users.txt", "w", encoding="utf-8") as dosya:
        user = input("Kullanici Adi Girin: ")
        password = input("Parola Girin: ")
        userList.append(dosya.write(user+":"+password))
        
    with open("users.txt", encoding="utf-8") as dosya:
        for satir in dosya:
            kontrol(satir)           
main()