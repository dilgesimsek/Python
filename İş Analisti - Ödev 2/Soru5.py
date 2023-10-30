sayi = int(input("Bir sayı girin: "))
asal_carpanlar = []

for i in range(2, sayi + 1):
    while sayi % i == 0:
        asal_carpanlar.append(i)
        sayi //= i

print("Asal Çarpanlar:", asal_carpanlar)
