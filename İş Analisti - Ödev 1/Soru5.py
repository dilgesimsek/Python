# Kullanıcıdan bir sayı alınması
sayi = input("Bir sayı girin: ")

# Girilen sayının tersini alarak kontrol edilmesi
ters_sayi = sayi[::-1]

# Palindrom kontrolü yapılması
if sayi == ters_sayi:
    print("Girilen sayı bir palindromdur.")
else:
    print("Girilen sayı bir palindrom değildir.")
