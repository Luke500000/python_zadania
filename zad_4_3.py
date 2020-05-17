"""### Zadanie 4.3 | Pociąg
​
Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość
 (początkowa wartość to 10) i ilosc_paliwa (początkowa wartość to 1000).
​
Dodaj do klasy `Pociag` metode `opis`. Ta metoda niech zwraca napis o treści
"Moja predkość to (ileś tam). Mam jeszcze (ileś tam) litrów paliwa." Dodatkowo zaimplementuj metodę `__str__`.
​
Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący,
 o ile ma zwiekszyć się prędkość. Ta metoda niech zwiększa predkość pociągu o tyle,
  ile jest powiedziane w argumencie. I niech zmniejsza ilość paliwa o: `(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.
​
Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75% (jeśli ktoś spróbuje tak zwiększyć prędkość, prędkość niech pozostaje po prostu bez zmian).
Niech nie da sie zwiększyć prędkości, jeśli pociąg nie ma juz paliwa
(jeśli ktoś spróbuje zwiększyć prędkość, kiedy nie ma paliwa, prędkość niech pozostaje po prostu bez zmian).
​
Przetestuj swoje rozwiązanie i napisz testy, w których:
- zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis
"""

class Pociag:
    def __init__(self):
        self.predkosc=10 #początkowa prędkość pociągu
        self.ilosc_paliwa=1000 #początkowa ilość paliwa pociągu

    def opis(self):
        """
        :return: Opis podstawowych parametrów pociągu
        """
        print( f"Moja predkość to {self.predkosc}. Mam jeszcze {self.ilosc_paliwa} litrów paliwa.")

    def __str__(self) -> str:
        return f"Moja predkość to {self.predkosc}. Mam jeszcze {self.ilosc_paliwa} litrów paliwa."

    def przyspiesz(self, przyrost:float):
        """
        :param przyrost: Przyrost prędkości pociągu [-]
        :return:
        """
        if self.ilosc_paliwa>0:
            if (przyrost/self.predkosc)<=0.75:
                tmp=self.predkosc
                self.predkosc+=przyrost
                self.ilosc_paliwa-=(self.predkosc-tmp) * (tmp / 100)

def test_inicjacja():
    z = Pociag()
    assert z.predkosc==10, z.ilosc_paliwa==1000

def test_przyspieszenie():
    z = Pociag()
    z.przyspiesz(5)
    assert z.predkosc==15, z.ilosc_paliwa==(1000-(15-10)*10/100)

def test_przyspieszenie2():
    z = Pociag()
    z.przyspiesz(5)
    z.przyspiesz(20)
    assert z.predkosc==15, z.ilosc_paliwa==(1000-(15-10)*10/100)

