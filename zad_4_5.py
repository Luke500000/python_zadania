"""### Zadanie 4.5 | Żółw
​Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie (wyrażone dwiema współrzędnymi)
i jakieś ustawienie, czyli kurs (wyznaczony pojedyncza liczba).
Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.
Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.
Metoda `idz` powoduje przejście żółwia o określoną odległość. Z klasy będzie się korzystać tak:
```python
z = Zolw(100, 100)
z.idz(50)
print(z) # ma sie wypisac: x=100, y=50
z.obroc_sie(90)
z.idz(50)
print(z) # ma sie wypisac: x=150, y=50
"""
import math

class Zolw:
    def __init__(self, x:float, y:float):
        """
        :param x: Współrzędna x żółwia [-]
        :param y: Współrzędna y żółwia [-]
        """
        self.x=x
        self.y=y
        self.kurs=0

    def obroc_sie(self, kat:float):
        """
        :param self:
        :param kat: Kąt obrotu żółwia, kierunek trygonometryczny, odwrotny do ruchu wsk. zegara [rad]
        :return:
        """
        self.kurs=kat*(math.pi/180)

    def idz(self, droga:float):
        """
        :param droga: Przemieszczenie żółwia [-]
        :return:
        """
        self.x+=droga*math.sin(self.kurs)
        self.y-=droga*math.cos(self.kurs)

    def __str__(self):
        return f"x={self.x:.2f}, y={self.y:.2f}"

def test_inicjacja():
    z = Zolw(100, 100)
    assert z.x==100, z.y==100

def test_przod():
    z = Zolw(100, 100)
    z.idz(50)
    assert z.x==100, z.y==50

def test_obrot():
    z = Zolw(100, 100)
    z.obroc_sie(180)
    z.idz(50)
    assert z.x==100, z.y==150

def test_obrot2():
    z = Zolw(100, 100)
    z.obroc_sie(90)
    z.idz(50)
    assert z.x==150, z.y==100
