sayi = int(input("Bir sayı girin: "))
asal = True

if sayi <= 1:
    asal = False
else:
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            asal = False
            break

if asal:
    print(sayi, "bir asal sayıdır.")
else:
    print(sayi, "bir asal sayı değildir.")
