
# Çarpım Tablosu

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("\n")


"""# 2. yol -farklı versiyon-
import time
# import winsound (Modül yüklü olmadığı için çalmadı)
for a in range (1, 11):
    print("\t")
    for b in range (1, 11):
        time.sleep(1)
        # winsound.Beep(1000, 100) (Modül yüklü olmadığı için çalmadı)
        print(f"{a} x {b} = {a * b}", end="\t")
"""

