number1 = 5
number2 = 10 

# operator perbandingan 
print(number1 != number2)

if number1 != number2:
    print("Nomer berbeda!")

else:
    print("Nomer sama!")

# Operator logika 
if number1 > 99 and number1 < 1000:
    print("Bilangan ratusan!")
else:
    print("Bukan bilangan ratusan!")

# Operator aritmatika 
while True:
    number3 = int(input("Masukan angka: "))

    if number3 ==00:
        break

    if number3 % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")