a = int(input("Masukan Bilangan 1:"))
b = int(input("Masukan Bilangan 2:"))
c = int(input("Masukan Bilangan 3:"))

maks = a
if b > maks:
    maks = b
if c > maks:
    maks = c
    
print()
print('Nilai yang terbesar adalah: %d' % maks)
