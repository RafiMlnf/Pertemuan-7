# Pertemuan 7 - Kondisional dan perulangan

**Praktikum 2 - Modul Praktikum 2**
-----------------------------------------------

Program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
tersebut tampilkan bilangan terbesarnya.

*1. Cetak nilai bilangan 1 sampai 3 yang akan di input*
```Python
a = int(input("Masukan Bilangan 1 : "))
b = int(input("Masukan Bilangan 2 : "))
c = int(input("Masukan Bilangan 3 : "))
```
*2. Lalu buat kondisi if dan cetak hasil maksimal `maks` seperti dibawah ini.  
Masukan a sebagai nilai maksimal, lalu masukan jika b adalah nilai maksimal maka b akan di cetak sebagai nilai terbesar begitu juga dengan c*
> *`%d` digunakan sebagai pengganti untuk nilai numerik atau desimal.*
```Python
maks = a
if b > maks:
    maks = b
if c > maks:
    maks = c
    
print()
print('Nilai yang terbesar adalah : %d' % maks)
```
  
*3. Run program dengan 3 kondisi inputan yang berbeda*
![Modul 2 - Praktikum 2](https://user-images.githubusercontent.com/115614668/200608482-b692e152-8b09-44c8-abca-1650642305f4.png)
![02  Modul 2 - Praktikum 2](https://user-images.githubusercontent.com/115614668/200609346-0897f372-759e-4cf3-8f60-2f2e72fc0d53.png)
![03  Modul 2 - Praktikum 2](https://user-images.githubusercontent.com/115614668/200609875-097514ef-8a8d-430d-a363-4eebba61531e.png)

**Flowchart Praktikum 2 - Modul 2**

----------------------------------------------
**Latihan 1 - Modul Praktikum 3**
----------------------------------------------

Membuat program bilangan acak yang lebih kecil dari 0.5

*1. Cetak nilai bilangan yang akan di input*  
*2. Gunakan fungsi `import random` terlebih dahulu*  
```Python
jumlah = int(input("Masukkan nilai n : "))
import random
for i in range (jumlah) :
    print("Data ke", i+1,"=",(random.uniform(0.1,0.5)))
```
*3. Angka yang di input akan mencetak jumlah seberapa banyaknya nilai data ke* `print("Data ke", i+1,"=",(random.uniform(0.1,0.5)))`  
*4. Cetak dengan rumus `i+1` untuk melakukan peningkatan nilai `+1` setiap banyaknya nilai input yang dimasukkan*  
> (0.1,0.5) gunanya untuk membatasi angka acak dari 0,1 sampai 0,5  

*5. Jalankan program*  

![01  Modul 3 - Latihan 1](https://user-images.githubusercontent.com/115614668/200617475-21b99516-95a2-42d2-bb16-68860314d151.png)

---------------------------------------------------
**Latihan 2 - Modul Praktikum 3**
----------------------------------------------

Program menampilkan bilangan terbesar dari n buah data yang diinputkan dan masukkan angka 0 untuk berhenti  

```Python
max = 0
while True:
    a=int(input("Masukan bilangan : "))
    if max < a:
        max = a
    if a ==0 :
        break

print()
print("Bilangan terbesar adalah :", max)
```
- Deklarasikan `max = 0`  
- Masukan `while True` adalah perulungan tak terbatas  
- Cetak input bilangan `a=int(input("Masukan bilangan : "))`  
- Buat kondisi if `max = a`
- Gunakan angka 0 sebagai fungsi break, dengan menginput angka 0, maka program akan terhenti  
- Cetak hasil bilangan terbesar dari kondisi `max`  
- Run Program   

![01  Latihan 2 - Modul 3](https://user-images.githubusercontent.com/115614668/200652421-6a890cbe-830a-4524-b609-c9bc82fb4b45.png)

---------------------------------------------------
**Program 1 - Modul Praktikum 3**
----------------------------------------------
Buat program sederhana dengan perulangan
```Python
modal = 100000000
laba = 0
untung = 0
for i in range(1,9,1):
    if(i<3):
        laba = 0
        untung = untung + laba
    elif(i<5):
     laba = modal*1/100
     untung = untung + laba
    elif(i<8):
     laba = modal*5/100
     untung = untung + laba
    else:
        laba = modal*2/100
        untung = untung + laba
    print("Laba Bulan ke-",i," Sebesar = Rp.",laba)
print("Total Laba Adalah : ",untung)
```
- Masukan integer  
`modal = 100000000`  
`laba = 0`  
`untung = 0`  
- Gunakan fungsi for `for i in range(1,9,1):`
    - Fungsi `(1,9`,1) adalah untuk membatasi angka dari 1 sampai 9, 
    - Sedangkan `,1)` untuk peningkatan 1 nilai setiap output dari `Laba bulan ke - ...`  
- Buat kondisi if/elif/else `(i<...)` untuk mengubah status pada bulan ke 3, 5, dan 8 
- Buat rumus `modal*.../100` dan `untung = untung + laba`
- Cetak hasil
```Python
  print("Laba Bulan ke-",i," Sebesar = Rp.",laba)
print("Total Laba Adalah : ",untung)
```
- Terakhir, run program   

![06  Program 1 - Modul 3](https://user-images.githubusercontent.com/115614668/200653302-0edb103c-4308-4de4-9a0a-4f92f0734f96.png)

---------------------------------------------------
**Latihan 1 - Struktur Kondisi**
----------------------------------------------
Program sederhada dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.
```Python
# Menentukan bilangan yang lebih besar
a = input("Masukan nilai a : ")
b = input("Masukan nilai b : ")

if a > b:
    print("Nilai", a ,"lebih besar dari", b)
else:
    print("Nilai", b ,"Lebih besar dari", a)
```
- Cetak input nilai bilangan  
`a = input("Masukan nilai a : ")`  
`b = input("Masukan nilai b : ")`  

- Buat kondisi if dan else  
```Python
a > b maka yang dicetak a lebih besar dari b

else adalah sebaliknya
b > a maka yang dicetak b lebih besar dari a
```

- Hasil run program :  

![07  Latihan 1 - Struktur Kondisi](https://user-images.githubusercontent.com/115614668/200654559-f508634f-33ec-4b86-a06a-a8ef89b2ab62.png)  

---------------------------------------------------
**Latihan 2 - Struktur Kondisi**
----------------------------------------------
Buat program untuk mengurutkan data berdasarkan input sejumlah data (minimal 3 variable input atau lebih), kemudian tampilkan hasilnya secara berurutan mulai dari data terkecil.
```Python
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
```
- Cetak masukan input bilangan 
```Python
print ("Masukkan 3 bilangan yang diinginkan!")
a = input("Bilangan 1 = ")
b = input("Bilangan 2 = ")
c = input("Bilangan 3 = ")
```
- Buat kondisi if/else/elif
```Python
b < c
Maka a adalah bilangan terkecil disusul b dan c
else : sebaliknya

b < a dan b < c
if   : a < c
Maka b adalah bilangan terkecil disusul b dan c atau c dan b
else : sebaliknya

if   : a < b
Maka c adalah bilangan terkecil disusul a dan b atau b dan a
else : sebaliknya
```

- Run program  

![08  Latihan 2 - Struktur Kondisi](https://user-images.githubusercontent.com/115614668/200654535-a97c84ba-e6bf-4adc-b6ba-1d7ac782b87c.png)  

---------------------------------------------------
**Latihan 1 - Perulangan**
----------------------------------------------
Program dengan perulangan bertingkat (nested)
```Python
for a in range(0, 10):
    for b in range (0, 10):
        print("{0:>3}".format(b + a), end=" ")
    print()
```
- Gunakan fungsi for `for a in range(0, 10):` `a`akan saya fungsikan sebagai kolom, begitu juga dengan `b` tapi akan saya gunakan sebagai baris
> `(0,10)` Berfungsi sebagai pembatas dari angka 0 sampai 10
- Cetak hasil menggunakan format `{0:>...}` Untuk memberi jarak setiap angka ke angka, dan beri rumus (b+a) untuk menjumlahkan angka kolom dan baris
- Run Program  

![09  Latihan 1 - Perulangan](https://user-images.githubusercontent.com/115614668/200654550-872b2f81-cf24-40cb-910f-4b5adbfbf03e.png)

---------------------------------------------------
**Latihan 2 - Perulangan**
----------------------------------------------
Membuat program bilangan acak yang lebih kecil dari 0.5

*1. Cetak nilai bilangan yang akan di input*  
*2. Gunakan fungsi `import random` terlebih dahulu*  
```Python
jumlah = int(input("Masukkan nilai n : "))
import random
for i in range (jumlah) :
    print("Data ke", i+1,"=",(random.uniform(0.1,0.5)))
```
*3. Angka yang di input akan mencetak jumlah seberapa banyaknya nilai data ke* `print("Data ke", i+1,"=",(random.uniform(0.1,0.5)))`  
*4. Cetak dengan rumus `i+1` untuk mencetak +1 setiap seberapa banyak nilai input yang dimasukkan*  
> (0.1,0.5) gunanya untuk membatasi angka acak dari 0,1 sampai 0,5  

*5. Jalankan program*  

![10  Latihan 2 - Perulangan](https://user-images.githubusercontent.com/115614668/200654557-00cded33-d30d-4531-9b65-f2e1f6e3e52d.png)  

---------------------------------------------------
Sekian
---------------------------------------------------
