sayi = int(input("Bir sayı girin: "))
toplam = 0

for i in range(1, sayi):
    if sayi % i == 0:
        toplam += i

if toplam == sayi:
    print(sayi, "bir mükemmel sayıdır.")
else:
    print(sayi, "bir mükemmel sayı değildir.")
