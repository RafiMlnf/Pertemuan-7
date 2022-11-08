max = 0
while True:
    a=int(input("Masukan bilangan : "))
    if max < a:
        max = a
    if a ==0 :
        break

print()
print("Bilangan terbesar adalah :", max)