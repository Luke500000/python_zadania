### Zadanie 1.6 | Bilety

wiek = int(input(f"Podaj wiek: "))
liczba_biletow = int(input(f"Podaj liczbę biletów: "))

#tupla_ceny = (0, 2.28, 3.8, 1.9) #stara wersja
#tupla_wiek = (0, 6, 7, 17, 18, 64, 65) #stara wersja
tupla = ((0,0,6),(2.28,7,17),(3.8,18,64),(1.9,65))

if tupla[0][1] < wiek <= tupla[0][2]:
    cena = liczba_biletow * tupla[0][0]
elif tupla[1][1] <= wiek <= tupla[1][2]:
    cena = liczba_biletow * tupla[1][0]
elif tupla[2][1] <= wiek <= tupla[2][2]:
    cena = liczba_biletow * tupla[2][0]
else:
    cena = liczba_biletow * tupla[3][0]

print(f"Wiek: {wiek}, liczba biletów: {liczba_biletow}, do zapłaty: {cena:.2f} zł.")