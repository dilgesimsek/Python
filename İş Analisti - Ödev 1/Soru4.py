# Kullanıcıdan dairenin yarıçapı alınması
yaricap = float(input("Dairenin yarıçapını girin: "))

# Dairenin alanının hesaplanması (π * r^2 formülü kullanılır)
alan = 3.14 * yaricap ** 2

# Dairenin çevresinin hesaplanması (2 * π * r formülü kullanılır)
cevre = 2 * 3.14 * yaricap

# Sonuçları ekrana yazdırın
print("Dairenin Alanı:", alan)
print("Dairenin Çevresi:", cevre)
