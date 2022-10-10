
# Palindromik Sayıları bulan python programı (1-1000 arası)

"""
Palindromik sayı, iki taraftan okunduğu zaman okunuş yönüyle aynı olan sayılardır.

Örnek: 1, 4, 8, 99, 101, 363, 4004, 9889, 13531 vb.
"""

# 1. Yöntem

def kontrol(num):
    if(str(num) == str(num)[::-1]):    # num'ın tersiyle aynı ise True döndür
        return True
    else:
        return False

for i in range(1, 1000):
    if(kontrol(i)):
        print(i, end=" ")

"""# 2. Yöntem
def palindrom(p, q):
    for q in range(len(p)):
        if p[q] != p[-q-1]:
            return False
    return True

for i in range(1, 1000):
    if palindrom(str(i), i):
        print(i, end=" ")"""




