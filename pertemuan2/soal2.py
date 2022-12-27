print('''Program Menghitung Nilai Rata - Rata
========================================''')
#Program Memasukkan banyaknya data dan Bilangan

jmlbil = int(input("-- Masukkan banyaknya data :"))

#Membuat garis baru
print()

#Program perhitungan dan perulangan
angka = []
jumlah = 0
for i in range (0, jmlbil):
    inpt = int(input("Masukkan Angka ke-%d: " % (i+1)))
    angka.append(inpt)
    jumlah += angka[i]
    rata2 = jumlah / jmlbil

#Membuat garis baru
print()

#Mencetak hasil rata2
print("-- Rata-rata = %0.2f" % rata2)

print('''========================================''')
