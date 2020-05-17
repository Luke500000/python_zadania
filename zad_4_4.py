"""### Zadanie 4.4 | Zbiornik
​
Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).
​
Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech odpowiednio dodają lub
odejmują tę liczbę do atrybutu `ilosc_wody`. Niech nie da się odlać więcej wody, niż jest w zbiorniku.
​
Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.
​
Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`. Metoda dolej oprócz argumentu `ile`
powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody.
Dolanie wody do zbiornika powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).
"""

class Zbiornik:
    def __init__(self):
        self.ilosc_wody=0
        self.temperatura=0


    def dolej(self, ile, temperatura:float):
        """
        :param ile:
        :param temperatura:
        :return:
        """
        tmp=self.ilosc_wody
        self.ilosc_wody += ile
        self.temperatura=(tmp*self.temperatura+ile*temperatura)/(tmp+ile)

    def odlej(self, ile:float):
        """
        :param ile:
        :return:
        """
        if ile>=self.ilosc_wody:
            ile=self.ilosc_wody
        self.ilosc_wody -= ile
        if self.ilosc_wody==0:
            self.temperatura=0

    def __str__(self)->str:
        return f"Zbiornik z {self.ilosc_wody} litrami wody o temperaturze {self.temperatura} st. C."

def test_inicjacja():
    z = Zbiornik()
    assert z.ilosc_wody==0, z.temperatura==0

def test_dolej():
    z = Zbiornik()
    z.dolej(10, 30)
    z.dolej(10, 10)
    assert z.ilosc_wody == 20, z.temperatura == 20

def test_odlej():
    z = Zbiornik()
    z.dolej(100, 30)
    z.odlej(50)
    assert z.ilosc_wody == 50, z.temperatura == 30

def test_odlej2():
    z = Zbiornik()
    z.dolej(100, 30)
    z.odlej(200)
    assert z.ilosc_wody == 0, z.temperatura == 30

def test_odlej3():
    z = Zbiornik()
    z.dolej(100, 30)
    z.odlej(100)
    assert z.ilosc_wody == 0, z.temperatura == 0