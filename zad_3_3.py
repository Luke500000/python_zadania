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
import pytest

def suma(lista_liczb:list)->float:
    """
    :param lista_liczb:
    :return: suma liczb z listy
    """
    suma = None
    for liczba in lista_liczb:
        if suma is None:
            suma = liczba
        else:
            suma += liczba
    return suma

def srednia(lista_liczb:list)->float:
    """
    :param lista_liczb: lista
    :return: srednia z liczb z listy
    """
    if len(lista_liczb) <= 0:
        raise ValueError("Pusta lista")
    suma = None
    for liczba in lista_liczb:
        if suma is None:
            suma = liczba
        else:
            suma += liczba
    return suma/len(lista_liczb)

def max(lista_liczb:list)->float:
    """
    :param lista_liczb:
    :return: max. liczba z liczb z listy
    """
    if len(lista_liczb) <= 0:
        raise ValueError("Pusta lista")
    maks = None
    for liczba in lista_liczb:
        if maks is None:
            maks = liczba
        else:
            if liczba >= maks:
                maks = liczba
    return maks

def roznica_min_max(lista_liczb:list)->float:
    """
    :param lista_liczb:
    :return: Różnica pomiędzy min, a max liczbą z liczb
    """
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

def wypisz_wieksze(lista_liczb:list, x:float):
    """
    :param lista_liczb:
    :param x: liczba minimalna
    :return: Printuje liczby większe od x
    """
    for liczba in lista_liczb:
        if liczba > x:
           print(liczba,end=" ")

def pierwsza_wieksza(lista_liczb:list, x:float):
    """
    :param lista_liczb:
    :param x: liczba minimalna
    :return: Printuje pierwszą liczbę większą od x
    """
    for liczba in lista_liczb:
        if liczba > x:
            return liczba
    return None

def suma_wiekszych(lista_liczb:list, x:float)->float:
    """
    :param lista_liczb:
    :param x: liczba minimalna
    :return: Suma liczb większych od x
    """
    suma = None
    for liczba in lista_liczb:
        if liczba > x:
            if suma is None:
                suma=liczba
            else:
                suma+=liczba
    return suma

def ile_wiekszych(lista_liczb:list, x:float)->float:
    """
    :param lista_liczb:
    :param x:
    :return: Libcza liczb wiekszych od x
    """
    ile = None
    for liczba in lista_liczb:
        if liczba > x:
            if ile is None:
                ile=1
            else:
                ile+=1
    return ile

def wypisz_podzielne(lista_liczb:list, x:float):
    """
    :param lista_liczb:
    :param x:
    :return:Printuje liczby podzielne przez x w liście
    """
    for liczba in lista_liczb:
        if liczba%x == 0:
            print(liczba,end=" ")


def pierwsza_podzielne(lista_liczb:list, x:float)->float:
    """
    :param lista_liczb:
    :param x:
    :return: Pierwsza podzielna liczba przez x w liście
    """
    for liczba in lista_liczb:
        if liczba%x == 0:
            return liczba
    return None

def znajdz_wspolny(lista1:list, lista2:list)->float:
    """
    :param lista1:
    :param lista2:
    :return: Liczba, która występuje w lista1 oraz lista2
    """
    for liczba1 in lista1:
        for liczba2 in lista2:
            if liczba1==liczba2:
                return liczba1
    return None

liczby = [10, 20, 30, 40]
liczby2 = [17, 13, 45, 19]

def test_suma():
    assert suma(liczby) == 100

def test_srednia():
    assert srednia(liczby) == 25

def test_srednia2():
    with pytest.raises(ValueError):
        srednia([])

def test_max():
    assert max(liczby) == 40

def test_max2():
    with pytest.raises(ValueError):
        max([])

def test_roznica():
    assert roznica_min_max(liczby) == 30

def test_wypisz_wieksze():
    assert wypisz_wieksze(liczby, 20) == print("30 40 ")

def test_pierwsza_wieksza():
    assert pierwsza_wieksza(liczby, 20) == 30

def test_suma_wieksza():
    assert suma_wiekszych(liczby, 20) == 70

def test_ile_wieksza():
    assert ile_wiekszych(liczby, 20) == 2

def test_wypisz_podzielne():
    assert wypisz_podzielne(liczby, 20) == print("20 40 ")

def test_pierwsza_podzielna():
    assert pierwsza_podzielne(liczby, 20) == 20

def test_pierwsza_podzielna2():
    assert pierwsza_podzielne(liczby, 100) == None

def test_znajdz_wspolne():
    assert znajdz_wspolny(liczby, liczby2) == None