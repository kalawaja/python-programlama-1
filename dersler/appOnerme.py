# Matematik Mantık Konusundaki Bileşik Önermeler ile ilgili Python Programı

# "VE" Bağlacı ile Yapılan Bileşik Önermeler
# "VEYA" Bağlacı ile Yapılan Bileşik Önermeler
# "YA DA" Bağlacı ile Oluşturulan Bileşik Önermeler
# "İSE" Bağlacı ile Oluşturulan Bileşik Önermeler
# "ANCAK VE ANCAK" Bağlacı ile Kurulan Bileşik Önermeler

# p için doğruluk değeri giriniz
inputP = int(input("p için doğruluk değeri giriniz: "))

# q için doğruluk değeri giriniz
inputQ = int(input("q için doğruluk değeri giriniz: "))

# p v q ≡ için doğruluk değerini yazdır
print("p ∨ q ≡ ", inputP + inputQ - (inputP * inputQ))

# p ^ q ≡ için doğruluk değerini yazdır
print("p ^ q ≡ ", inputP * inputQ)

# p ⊻ q ≡ için doğruluk değerini yazdır
print("p ⊻ q ≡ ", inputP + inputQ - 2 * (inputP * inputQ))

# p → q ≡ için doğruluk değerini yazdır
print("p → q ≡ ", 1 - inputP + inputQ)

# p ↔ q ≡ için doğruluk değerini yazdır
print("p ↔ q ≡ ", 1 - abs(inputP - inputQ))

# p ⇒ q önermesinin karşıtı q ⇒ p
print("p ⇒ q önermesinin karşıtı q ⇒ p ≡ ", 1 - inputP + inputQ)

# p ⇒ q önermesinin tersi p’ ⇒ q’
print("p ⇒ q önermesinin tersi p’ ⇒ q’ ≡ ", inputP - inputQ)

# p ⇒ q önermesinin karşıt tersi q’ ⇒ p’
print("p ⇒ q önermesinin karşıt tersi q’ ⇒ p’ ≡ ", inputP - inputQ)

# De Morgan (p ^ q)' ≡ p' ∨ q' için doğruluk değerini yazdır
print("(p ^ q)' ≡ p' ∨ q' ≡ ", 1 - inputP + 1 - inputQ)

# De Morgan (p ∨ q)' ≡ p' ^ q' için doğruluk değerini yazdır
print("(p ∨ q)' ≡ p' ^ q' ≡ ", 1 - inputP * 1 - inputQ)