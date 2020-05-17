"""### Zadanie 4.6 | Kółko i krzyżyk
​
Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.
​Ma ona mieć metody:
`dodaj_element(x: int, y: int, rodzaj_elementu)`
W argumencie `rodzaj_elementu` będzie napis `"x"` lub `"y"`. Jeśli ruch jest nieprawidłowy, metoda powinna zwracać fałsz.
​
`stan_gry()` - Ta metoda ma zwracać liczbę oznaczającą stan gry (gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona sukcesem kółek).
​`czyj_ruch()` - Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).
​
Wyświetlenie obiektu tej klasy ma wypisać planszę. Użyj tej klasy do zrobienia gry w kółko i krzyżyk.
"""
class PlanszaXO:
    def __init__(self):
        self.start=False #znacznik rozpoczecia gry
        self.slownik=dict() #slownik z plansza
        self.ostatni_element=None #ostatni element, np. 'O' lub 'X'
        for liczba in range(3):
            for liczba2 in range(3):
                self.slownik[liczba+1,liczba2+1]="-"

    def dodaj_element(self,x: int, y: int, rodzaj_elementu:str):
        """
        :param x: Wsp. x planszy z lewej do prawej
        :param y: Wsp. y planszy z góry do dołu
        :param rodzaj_elementu: 'O' lub 'X'
        :return:
        """
        self.start=True
        if (1<=x<=3 and 1<=y<=3 and (rodzaj_elementu=="O" or rodzaj_elementu=="X")):
            self.slownik[x,y]=rodzaj_elementu
            self.ostatni_element=rodzaj_elementu
            return True
        else:
            return False

    def stan_gry(self):
        #1 - koniec gry, zwycięstwo kółko
        #2 - koniec gry, zwycięstwo krzyżyk
        #3 - gra trwa
        #4 - gra jeszcze nie ruszyła
        lista=[1,2,3]
        if self.start==True:
            if self.slownik[lista[0], lista[0]]=="O" and self.slownik[lista[1], lista[1]]=="O"  and self.slownik[lista[2], lista[2]]=="O":
                return 1
            if self.slownik[lista[0], lista[-1]]=="O"  and self.slownik[lista[1], lista[-2]]=="O"  and self.slownik[lista[2], lista[-3]]=="O":
                return 1
            if self.slownik[lista[0], lista[0]]=="X" and self.slownik[lista[1], lista[1]]=="X"  and self.slownik[lista[2], lista[2]]=="X":
                return 2
            if self.slownik[lista[0], lista[-1]]=="X"  and self.slownik[lista[1], lista[-2]]=="X"  and self.slownik[lista[2], lista[-3]]=="X":
                return 2
            for liczba in range(3):
                if self.slownik[liczba+1,lista[0]]=="O"  and self.slownik[liczba+1,lista[1]]=="O"  and self.slownik[liczba+1,lista[2]]=="O":
                    return 1
                if self.slownik[lista[0],liczba+1]=="O"  and self.slownik[lista[1],liczba+1]=="O"  and self.slownik[lista[2],liczba+1]=="O":
                    return 1
                if self.slownik[liczba+1,lista[0]]=="X"  and self.slownik[liczba+1,lista[1]]=="X"  and self.slownik[liczba+1,lista[2]]=="X":
                    return 2
                if self.slownik[lista[0],liczba+1]=="X"  and self.slownik[lista[1],liczba+1]=="X"  and self.slownik[lista[2],liczba+1]=="X":
                    return 2
            return 3
        else:
            return 4

    def czyj_ruch(self):
        if self.stan_gry()==3 or self.stan_gry()==4:
            if self.ostatni_element=="O":
                print("Ruch ma krzyżyk")
            elif self.ostatni_element=="X":
                print("Ruch ma kółko")
            else:
                print("Początek gry: ruch ma kółko lub krzyżyk")
        elif self.stan_gry() == 1 or self.stan_gry() == 2:
            print("Gra się zakończyła, koniec ruchów")

    def __str__(self):
        self.opisz()
        return " "

    def opisz(self):
        for liczba in range(3):
            for liczba2 in range(3):
                print(self.slownik[liczba+1,liczba2+1],end=" ")
            if liczba2==2:
                print()

def test_inicjalizacja():
    a = PlanszaXO()
    assert a.stan_gry()==4

def test_planszy():
    a = PlanszaXO()
    assert a.stan_gry()==4

def test_pierwszy_ruch():
    a = PlanszaXO()
    a.dodaj_element(1, 1, "O")
    assert a.slownik[1,1] == "O" and a.dodaj_element(1, 1, "O")==True

def test_zly_element():
    a = PlanszaXO()
    a.dodaj_element(1, 1, "P")
    assert a.dodaj_element(1, 1, "P")==False

def test_zwyciestwo_krzyzyk():
    a = PlanszaXO()
    a.dodaj_element(1, 1, "X")
    a.dodaj_element(2, 1, "X")
    a.dodaj_element(3, 1, "X")
    assert a.stan_gry()==2


