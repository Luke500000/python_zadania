### Zadanie 1.6 | Bilety

wiek = int(input(f"Podaj wiek: "))
liczba_biletow = int(input(f"Podaj liczbę biletów: "))

tupla_ceny = (0, 2.28, 3.8, 1.9)
tupla_wiek = (0, 6, 7, 17, 18, 64, 65)

if tupla_wiek[0] < wiek <= tupla_wiek[1]:
    cena = liczba_biletow * tupla_ceny[0]
elif tupla_wiek[2] <= wiek <= tupla_wiek[3]:
    cena = liczba_biletow * tupla_ceny[1]
elif tupla_wiek[4] <= wiek <= tupla_wiek[5]:
    cena = liczba_biletow * tupla_ceny[2]
else:
    cena = liczba_biletow * tupla_ceny[3]

print(f"Wiek: {wiek}, liczba biletów: {liczba_biletow}, do zapłaty: {cena:.2f} zł.")