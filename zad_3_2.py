""""### Zadanie 3.2 | Miesiące
​Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
​Logikę obliczania liczby dni wydziel do osobnej funkcji.
​**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
​**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie."""
def ile_dni(miesiac:int, rok:int=2001)->int:
    """
    :param miesiac: Miesiąc w formie 1-12
    :param rok: Rok
    :return: Liczba dni w danym miesiącu danego roku
    """
    dni = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    dni_przestepne = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if ((rok%4==0 and rok%100!=0) or rok%400==0):
        wynik = dni_przestepne[miesiac-1]
    else:
        wynik = dni[miesiac-1]
    return wynik

def test_normalny():
    assert ile_dni(2,2001)==28

def test_normalny2():
    assert ile_dni(12,2001)==31

def test_przestepny():
    assert ile_dni(2,2000)==29

def test_przestepny2():
    assert ile_dni(12,2000)==31



