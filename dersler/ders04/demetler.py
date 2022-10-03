
demet = ("yazıcı", "mouse", "yazıcı", "tarayıcı", "ekran")

print(demet.count("yazıcı")) # 2 
# Count: istenilen elemanın kaç defa geçtiğini verir

print(type(demet)) # <class 'tuple'> 
# Type: veri tipini verir

print(sorted(demet)) # ['ekran', 'mouse', 'tarayıcı', 'yazıcı', 'yazıcı'] 
# Sorted: sıralar

print(demet.index("tarayıcı")+1) # 4 
# Index: istenilen elemanın kaçıncı sırada olduğunu verir

print(demet[::-1]) # ('ekran', 'tarayıcı', 'yazıcı', 'mouse', 'yazıcı') #Demetleri ters çevirir