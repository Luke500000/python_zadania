### Zadanie 1.7 | Liczenie cen

przedmiot = input(f"Co chcesz kupić? ")
cena = float(input(f"Podaj cenę za 1 jednostkę w zł: "))
ilosc = float(input(f"Podaj liczbę jednostek towaru: "))
koszt = cena * ilosc
print(f"Za {przedmiot}, który chcesz kupić zapłacisz: {koszt:.2f} zł.")