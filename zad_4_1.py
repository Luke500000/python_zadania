"""### Zadanie 4.1 | Ogłoszenia
​Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia
(takie jak w serwisie internetowym z ogłoszeniami).
​Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy,
które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.
"""
import random

class Ogloszenia:
    lista_id = set() #lista do przechowywania id dla klasy
    def __init__(self, tytul:str, opis:str, cena:float, mail_kontakt:str, dane_sprzedawcy:str, tel_kontakt:str):
        """
        :param tytul: Tytuł ogłoszenia
        :param opis: Opis ogłoszenia
        :param cena: Cena ogłoszenia
        :param mail_kontakt: Mail sprzedawcy
        :param dane_sprzedawcy: Imię i nazwisko sprzedawcy
        :param tel_kontakt: Telefon kontaktowy
        """
        self.tytul=tytul
        self.opis=opis
        self.cena=cena
        self.mail_kontakt=mail_kontakt
        self.dane_sprzedawcy=dane_sprzedawcy
        self.tel_kontakt=tel_kontakt
        self.id = self.przydziel_id(Ogloszenia.lista_id)

    def przydziel_id(self, lista_id:set):
        """
        :param lista_id: kolekcja id
        :return: id ogłoszenia
        """
        #wybor unikalnego id ogloszenia poprzez losowanie int'a z zakresu
        liczba = random.randint(1, 1000000000)
        while liczba in lista_id:
            liczba = random.randint(1, 1000000000)
        lista_id.add(liczba)
        return liczba

    def print_info(self):
        print(self.get_info())

    def get_info(self) -> str:
        return f"Ogloszenie ID: {self.id}, tytuł: {self.tytul}, opis: {self.opis}\n cena:{self.cena}, dane sprzedawcy: {self.dane_sprzedawcy}, {self.tel_kontakt}, {self.mail_kontakt}"

    def __str__(self):
        return self.get_info()

def test_ilosci_ogloszen():
    a = Ogloszenia("Sprzedam lozko", "Sprzedam lozko pietrowe", 3000, "opo@opo.pl", "Adam Kowal", "723-454-345")
    b = Ogloszenia("Sprzedam lozko", "Sprzedam lozko pietrowe", 3000, "opo@opo.pl", "Adam Kowal", "723-454-345")
    c = Ogloszenia("Sprzedam lozko", "Sprzedam lozko pietrowe", 3000, "opo@opo.pl", "Adam Kowal", "723-454-345")
    d = Ogloszenia("Sprzedam lozko", "Sprzedam lozko pietrowe", 3000, "opo@opo.pl", "Adam Kowal", "723-454-345")
    assert len(Ogloszenia.lista_id)==4

def test_poprawnosci_ogloszenia():
    e = Ogloszenia("Sprzedam lozko", "Sprzedam lozko pietrowe", 3000, "opo@opo.pl", "Adam Kowal", "723-454-345")
    assert e.tytul=="Sprzedam lozko" and e.opis=="Sprzedam lozko pietrowe" and e.cena==3000 and e.tel_kontakt=="723-454-345"
