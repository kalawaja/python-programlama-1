
with open("python-programlama-1/dersler/ders12/copy-write/first.txt", encoding="utf-8") as konudosyasi:
    with open("python-programlama-1/dersler/ders12/copy-write/second.txt", "a", encoding="utf-8") as yazdirmadosyasi:
        for satir in konudosyasi:
            print(satir, file=yazdirmadosyasi)