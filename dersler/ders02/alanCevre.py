
# Dairenin Alanı ve Çevfresini Hesaplayan Python Programı
# Dairenin Alanı    : πr²
# Dairenin Çevresi  : πr

pi = 3.14
yaricap = int(input("Dairenin Yarıçapını Giriniz: "))
alan = pi * yaricap ** 2
cevre = 2 * pi * yaricap

print("Alan: ", round(alan, 1))
print("Çevre: ", round(cevre))

''' # 2. yol
print(f"""
    Dairenin Alanı  : {alan}
    Dairenin Çevresi: {cevre}
""")
'''

''' # 3. yol
from math import pi
'''


