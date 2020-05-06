'''### Zadanie 3.3 | Operacje na listach
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
- `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma'''

def suma(lista_liczb):
    suma = None
    for liczba in lista_liczb:
        if suma is None:
            suma = liczba
        else:
            suma += liczba
    return suma

def srednia(lista_liczb):
    suma = None
    for liczba in lista_liczb:
        if suma is None:
            suma = liczba
        else:
            suma += liczba
    return suma/len(lista_liczb)

def max(lista_liczb):
    maks = None
    for liczba in lista_liczb:
        if maks is None:
            maks = liczba
        else:
            if liczba >= maks:
                maks = liczba
    return maks

def roznica_min_max(lista_liczb):
    maks = None
    minn = None
    if len(lista_liczb)==0:
        return 0
    else:
        for liczba in lista_liczb:
            if maks is None and minn is None:
                maks = liczba
                minn = liczba
            else:
                if liczba > maks:
                    maks = liczba
                if liczba < minn:
                    minn = liczba
        return maks - minn

def wypisz_wieksze(lista_liczb, x):
    for liczba in lista_liczb:
        if liczba > x:
           print(liczba,end=" ")

def pierwsza_wieksza(lista_liczb, x):
    for liczba in lista_liczb:
        if liczba > x:
            return liczba
    return None

def suma_wiekszych(lista_liczb, x):
    suma = None
    for liczba in lista_liczb:
        if liczba > x:
            if suma is None:
                suma=liczba
            else:
                suma+=liczba
    return suma

def ile_wiekszych(lista_liczb, x):
    ile = None
    for liczba in lista_liczb:
        if liczba > x:
            if ile is None:
                ile=1
            else:
                ile+=1
    return ile

def wypisz_podzielne(lista_liczb, x):
    for liczba in lista_liczb:
        if liczba%x == 0:
            print(liczba,end=" ")


def pierwsza_podzielne(lista_liczb, x):
    for liczba in lista_liczb:
        if liczba%x == 0:
            return liczba
    return None

def znajdz_wspolny(lista1, lista2):
    for liczba1 in lista1:
        for liczba2 in lista2:
            if liczba1==liczba2:
                return liczba1
    return None

print("Lista nr 1")
liczby = [10, 20, 30, 40]
{print(wartosc,end=" ") for wartosc in liczby}
print()
print(f"Suma liczb: {suma(liczby)}.")
print(f"Srednia liczb: {srednia(liczby)}.")
print(f"Max liczb: {max(liczby)}.")
print(f"Roznica min-max liczb: {roznica_min_max(liczby)}.")
wart=float(input("Podaj liczbe: "))
print(f"Wypisz wiekszą od: {wart}:")
wypisz_wieksze(liczby,wart)
print()
print(f"Wypisz pierwsza wiekszą od:{wart} : {pierwsza_wieksza(liczby,wart)}.")
print(f"Suma wiekszych od:{wart}: {suma_wiekszych(liczby,wart)}.")
print(f"Ile wiekszych od:{wart}: {ile_wiekszych(liczby,wart)}.")
dzielnik=float(input("Podaj dzielnik: "))
print(f"Wypisz podzielne przez {dzielnik}:")
wypisz_podzielne(liczby,dzielnik)
print()
print(f"Pierwsza podzielna przez {dzielnik}: {pierwsza_podzielne(liczby,dzielnik)}.")
print("Lista nr 2")
liczby2 = [17, 13, 45, 19]
{print(wartosc,end=" ") for wartosc in liczby2}
print()
print(f"Znajdź wspolne liczby w liście nr 1 i 2: {znajdz_wspolny(liczby, liczby2)}.")
