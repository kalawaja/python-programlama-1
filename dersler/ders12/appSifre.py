
# Kullanıcı adı ve şirfrei gir
# a methodu ile kullanıcı adı ve şifre kontrol edilir
# eğer kullanıcı adı ve şifre doğruysa, kullanıcı adı ve şifre bilgileri ekrana yazdırılır
# eğer kullanıcı adı ve şifre yanlışsa, kullanıcıya hata mesajı verilir

# kullanıcı adı ve şifre bilgisi gir
kullaniciAdi = input("Kullanıcı adı giriniz: ")
sifre = input("Şifre giriniz: ")

# kullanıcı adı ve şifre kontrol edilir
def kontrol(kullaniciAdi, sifre):
    if kullaniciAdi == "admin" and sifre == "123456":
        print("Kullanıcı adı ve şifre doğru.")
        print("Kullanıcı adı: ", kullaniciAdi)
        print("Şifre: ", sifre)
    else:
        print("Kullanıcı adı ve şifre yanlış.")

# kullanıcı adı ve şifre kontrol edilir
kontrol(kullaniciAdi, sifre)