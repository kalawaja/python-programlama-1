
from datetime import datetime as dt

# datetime.now() fonksiyonu ile tarih ve saat bilgilerini alabiliriz.

print("Sistem Tarihi ve Saati: ", dt.now())

"""tarih = dt.now()
print(tarih)"""

# datetime.strftime() fonksiyonu ile tarih ve saat bilgilerini istediğimiz formatta yazdırabiliriz.

print("Sistem Tarihi ve Saati: ", dt.now().strftime("%d/%m/%Y %H:%M:%S"))


"""from datetime import datetime as dt

print("Sistem Tarihi ve Saati: ", dt.now())

simdi = dt.now()

ay = simdi.month
print(ay, type(ay))"""