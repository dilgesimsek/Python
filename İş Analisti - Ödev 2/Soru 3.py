import math

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

ebob = math.gcd(sayi1, sayi2)
ekok = abs(sayi1 * sayi2) // ebob

print("EBOB:", ebob)
print("EKOK:", ekok)