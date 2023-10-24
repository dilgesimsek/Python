# Kullanıcıdan mevcut maaşı ve zam oranı alınması
maas = float(input("Mevcut maaşı girin: "))
zam_orani = float(input("Zam oranını girin (örneğin, %10 için 10 yazın): "))

# Zam oranını yüzde cinsine çevirilmesi
zam_orani_yuzde = zam_orani / 100

# Zam yapılmış maaş hesaplaması
zamli_maas = maas * (1 + zam_orani_yuzde)

# Sonucun ekrana yazdırılması
print("Zamli maaş: ", zamli_maas)
