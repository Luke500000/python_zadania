"""## 3. Funkcje
​Przy pisaniu wszystkich funkcji pamiętaj o `type-hinting`, `docstring` i stworzeniu testów do weryfikacji czy funkcja działa poprawnie.

Zadanie 3.1 Funkcje liczbowe
​Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
​1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry
​Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik."""

import math

def stopy_na_metry(stopy: float) -> float:
    """
    :param stopy:
    :return: stopy na metry
    """
    wynik = 0.3048 * stopy
    return wynik

def max(liczba1: float, liczba2: float) -> float:
    """
    :param liczba1:
    :param liczba2:
    :return: Max z liczb
    """
    if liczba1 > liczba2:
        return liczba1
    else:
        return liczba2

def srednia(liczba1: float, liczba2: float) -> float:
    """
    :param liczba1:
    :param liczba2:
    :return: Średnia z liczb
    """
    srednia = (liczba1 + liczba2) / 2
    return srednia

def pole_kola(promien: float) -> float:
    """
    :param promien:
    :return: Pole koła
    """
    pole = math.pi * (promien ** 2)
    return pole

def bmi(wzrost: float, waga: float) -> float:
    """
    :param wzrost: w m
    :param waga: w m
    :return: BMI
    """
    wynik = waga * (wzrost ** 2)
    return wynik

def pole_trojkata(a: float, b: float, c: float) -> float:
    """
    :param a: dlugosc boku a
    :param b: dlugosc boku b
    :param c: dlugosc boku c
    :return: Pole trójkąta z wzoru Herona
    """
    obwod = (a + b + c) / 2
    pole = (obwod * (obwod - a) * (obwod - b) * (obwod - c)) ** (0.5)
    return pole

def kilometry_na_mile(kilometry: float) -> float:
    """
    :param kilometry:
    :return: kilometry na mile
    """
    wynik = kilometry / 0.621371192
    return wynik

def mile_na_kilometry(mile: float) -> float:
    """
    :param mile:
    :return: mile na kilometry
    """
    wynik = mile * 0.621371192
    return wynik

# Testy
def test_basic():
    assert stopy_na_metry(1) == 0.3048 * 1

def test_basic1():
    assert max(2, 1) == 2

def test_basic2():
    assert srednia(1, 1) == 1

def test_basic3():
    assert pole_kola(1) == math.pi*(1**2)

def test_basic4():
    assert bmi(1.8, 100) == 100 * (1.8 ** 2)

def test_basic5():
    assert pole_trojkata(4,5,7) == 4*((6)**(1/2))

def test_basic6():
    assert kilometry_na_mile(1) == 1 / 0.621371192

def test_basic7():
    assert mile_na_kilometry(1) == 0.621371192
