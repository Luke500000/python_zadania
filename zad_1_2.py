# Zadanie 1.2 | Buty do szewca

import math

print(f"Nazewnictwo: poniedzialek, wtorek, sroda, czwartek, piatek, sobota, niedziela")
print(f"Skróty: pon, wt, sr, czw, ptk, sob, niedz")
dzien_tyg = input(f"Podaj dzień tygodnia, w którym oddano buty do szewca (zastosuj nazewnictwo lub skroty powyżej): ")

if dzien_tyg == "pon" or dzien_tyg == "poniedzialek":
    dzien_liczba = 1
elif dzien_tyg == "wt" or dzien_tyg == "wtorek":
    dzien_liczba = 2
elif dzien_tyg == "sr" or dzien_tyg == "sroda":
    dzien_liczba = 3
elif dzien_tyg == "czw" or dzien_tyg == "czwartek":
    dzien_liczba = 4
elif dzien_tyg == "ptk" or dzien_tyg == "piatek":
    dzien_liczba = 5
elif dzien_tyg == "sob" or dzien_tyg == "sobota":
    dzien_liczba = 6
elif dzien_tyg == "niedz" or dzien_tyg == "niedziela":
    dzien_liczba = 7
else:
    print(f"Wprowadziłeś niewłaściwy dzien tygodnia")
    print(f"KONIEC programu")
    exit()

czas_naprawy = int(input(f"Ile dni będzie trwała naprawa? "))
dzien_odbioru = dzien_liczba + czas_naprawy

while dzien_odbioru > 7:
    dzielnik = math.floor(dzien_odbioru / 7)
    #print(f"Dzielnik: {dzielnik}")
    dzien_odbioru-=dzielnik * 7
    #print(f"Dzien odbioru: {dzien_odbioru}")
if dzien_odbioru == 1:
    print(f"Dzień odbioru: Poniedziałek")
elif dzien_odbioru == 2:
    print(f"Dzień odbioru: Wtorek")
elif dzien_odbioru == 3:
    print(f"Dzień odbioru: Środa")
elif dzien_odbioru == 4:
    print(f"Dzień odbioru: Czwartek")
elif dzien_odbioru == 5:
    print(f"Dzień odbioru: Piątek")
elif dzien_odbioru == 6:
    print(f"Dzień odbioru: Sobota")
elif dzien_odbioru == 7:
    print(f"Dzień odbioru: Niedziela")
else:
    print(f"Wystąpił błąd")
