# Kullanıcıdan boy ve ağırlık değerlerinin alınması
boy = float(input("Boyunuzu (metre cinsinde) girin: "))
agirlik = float(input("Ağırlığınızı (kilogram cinsinde) girin: "))

# Vücut kitle endeksinin hesaplanması
vki = agirlik / (boy ** 2)

# Sonucu ekrana yazdırın
print("Vücut Kitle Endeksiniz:", vki)