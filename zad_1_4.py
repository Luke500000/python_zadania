wiek = int(input(f"Podaj wiek: "))
liczba_dni = int(input(f"Podaj liczbę dni w hotelu: "))

tupla_ceny = (100, 200, 180, 150)

if wiek < 18:
    oplata = tupla_ceny[0] * liczba_dni
else:
    if liczba_dni == 1:
        oplata = tupla_ceny[1] * liczba_dni
    elif 2 <= liczba_dni < 5:
        oplata = tupla_ceny[2] * liczba_dni
    else:
        oplata = tupla_ceny[3] * liczba_dni
    if wiek > 65:
        oplata *= 0.9

print(f"Oplata wynosi: {oplata:.2f} zł.")
