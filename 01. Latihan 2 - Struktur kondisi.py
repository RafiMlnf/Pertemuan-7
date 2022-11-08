# Mengurutkan 3 nilai dari terkecil ke terbesar

print ("Masukkan 3 bilangan yang diinginkan!")
a = input("Bilangan 1 = ")
b = input("Bilangan 2 = ")
c = input("Bilangan 3 = ")

if a<b and a<c:
    if b < c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b<a and b<c:
    if a<c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a<b:
        print(c, a, b)
    else:
        print(c, b, a)
