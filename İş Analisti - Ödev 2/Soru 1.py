fibonacci_serisi = [1, 1]
while len(fibonacci_serisi) < 20:
    yeni_sayi = fibonacci_serisi[-1] + fibonacci_serisi[-2]
    fibonacci_serisi.append(yeni_sayi)

print("Fibonacci Serisi ilk 20 eleman:", fibonacci_serisi)
