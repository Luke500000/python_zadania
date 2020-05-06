""""### Zadanie 3.2 | Miesiące
​Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
​Logikę obliczania liczby dni wydziel do osobnej funkcji.
​**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
​**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie."""
def ile_dni(miesiac:int, rok=2001) ->int:
    dni = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    dni_przestepne = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if ((rok%4==0 and rok%100!=0) or rok%400==0):
        wynik = dni_przestepne[miesiac-1]
    else:
        wynik = dni[miesiac-1]
    return wynik

print("Liczba dni w miesiacu")
print("Objaśnienie: styczeń = 1, luty = 2, marzec = 3, ..., grudzień = 12")
miesiac=int(input("Podaj miesiac: "))
if miesiac == 2:
    rok=int(input("Podaj rok: "))
    print(f"Liczba dni: {ile_dni(miesiac,rok)}")
else:
    print(f"Liczba dni: {ile_dni(miesiac)}")