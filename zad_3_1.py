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
    wynik = 0.3048 * stopy
    return wynik

def max(liczba1: float, liczba2: float) -> float:
    if liczba1 > liczba2:
        return liczba1
    else:
        return liczba2

def srednia(liczba1: float, liczba2: float) -> float:
    srednia = (liczba1 + liczba2) / 2
    return srednia

def pole_kola(promien: float) -> float:
    pole = math.pi * (promien ** 2)
    return pole

def bmi(wzrost: float, waga: float) -> float:
    wynik = waga * (wzrost ** 2)
    return wynik

def pole_trojkata(a: float, b: float, c: float) -> float:
    obwod = (a + b + c) / 2
    pole = (obwod * (obwod - a) * (obwod - b) * (obwod - c)) ** (0.5)
    return pole

def kilometry_na_mile(kilometry: float) -> float:
    wynik = kilometry / 0.621371192
    return wynik

def mile_na_kilometry(mile: float) -> float:
    wynik = mile * 0.621371192
    return wynik

# Testy
def test_basic():
    assert max(1, 2) == 2

def test_basic1():
    assert srednia(1, 1) == 1

print("Stopy na metry:")
stopy = float(input(f"Podaj liczbę stóp:"))
print(f"W metrach to: {stopy_na_metry(stopy)}.")
print("Liczba większa:")
liczba1 = float(input(f"Podaj liczbę nr 1:"))
liczba2 = float(input(f"Podaj liczbę nr 2:"))
print(f"Wieksza liczba to: {max(liczba1, liczba2)}.")
print("Srednia dwóch liczb:")
liczba1 = float(input(f"Podaj liczbę nr 1:"))
liczba2 = float(input(f"Podaj liczbę nr 2:"))
print(f"Srednia liczb to: {srednia(liczba1, liczba2)}.")
print("Pole kola:")
promien = float(input(f"Podaj promien:"))
print(f"Pole kola to: {pole_kola(promien)}.")
print("BMI:")
waga = float(input(f"Podaj wage:"))
wzrost = float(input(f"Podaj wzrost:"))
print(f"BMI to: {bmi(wzrost, waga)}.")
print("Pole trojkata:")
a = float(input(f"Podaj bok a:"))
b = float(input(f"Podaj bok b:"))
c = float(input(f"Podaj bok c:"))
print(f"Pole trojkata to: {pole_trojkata(a, b, c)}.")
print("km na mile:")
km = float(input(f"Podaj liczbe km:"))
print(f"Pole trojkata to: {kilometry_na_mile(km)}.")