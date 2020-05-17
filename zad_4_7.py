"""### Zadanie 4.7 | Ogłoszenia / dziedziczenie
​
Do zadania z klasą `Ogloszenie` dodaj kolejne kolejne klasy, które po niej dziedziczą.
​
`OgloszenieSamochodowe` – dziedziczy z `Ogloszenie` i dodatkowo określa cechy sprzedawanego samochodu jak
model, markę, rok produkcji, przebieg, pojemność, moc i rodzaj paliwa.
`OgloszenieMieszkaniowe` – też dziedziczy z `Ogloszenie`, a dodatkowo cechy sprzedawanego mieszkania / domu: miejscowość, metraż, liczba pokoi.
"""
from zad_4_1 import Ogloszenia

class OgloszenieSamochodowe(Ogloszenia):
    def __init__(self, tytul: str, opis: str, cena: float, mail_kontakt: str, dane_sprzedawcy: str, tel_kontakt: str,
                 marka:str, model:str, rok:int, przebieg:int, pojemnosc:int, moc:int, paliwo:str):
        """
        :param tytul: Tytuł ogłoszenia
        :param opis:  Opis ogłoszenia
        :param cena: Cena w PLN
        :param mail_kontakt: Adres mailowy
        :param dane_sprzedawcy: Imię i nazwisko
        :param tel_kontakt: Numer telefonu
        :param marka: Marka samochodu
        :param model: Model samochodu
        :param rok: Rok produkcji
        :param przebieg: Przebieg w km
        :param pojemnosc: Pojemnosc w cm3
        :param moc: Moc w KM
        :param paliwo: Rodzaj paliwa, np. benzyna
        """
        super().__init__(tytul, opis, cena, mail_kontakt, dane_sprzedawcy, tel_kontakt)
        self.model=model
        self.marka=marka
        self.rok=rok
        self.przebieg=przebieg
        self.pojemnosc=pojemnosc
        self.moc=moc
        self.paliwo=paliwo

    def print_info(self):
        print(self.get_info())

    def get_info(self) -> str:
        return f"Ogloszenie ID: {self.id}, tytuł: {self.tytul}, opis: {self.opis}\n cena: {self.cena}, " \
               f"dane sprzedawcy: {self.dane_sprzedawcy}, {self.tel_kontakt}, {self.mail_kontakt}, " \
               f"{self.marka}, {self.model}, {self.rok}r., {self.przebieg}km, {self.pojemnosc}cm3, {self.moc}KM, {self.paliwo}."

    def __str__(self):
        return self.get_info()

class OgloszenieMieszkaniowe(Ogloszenia):
    def __init__(self, tytul: str, opis: str, cena: float, mail_kontakt: str, dane_sprzedawcy: str, tel_kontakt: str,
                 miejscowosc:str, metraz:float, liczba_pokoi:int):
        """
        :param tytul: Tytuł ogłoszenia
        :param opis: Opis ogłoszenia
        :param cena: Cena w PLN
        :param mail_kontakt: Adres mailowy
        :param dane_sprzedawcy: Imię i nazwisko
        :param tel_kontakt: Numer telefonu
        :param miejscowosc: Miejscowość
        :param metraz: Powierzchnia w m2
        :param liczba_pokoi: Liczba pokoi
        """
        super().__init__(tytul, opis, cena, mail_kontakt, dane_sprzedawcy, tel_kontakt)
        self.miejscowosc=miejscowosc
        self.metraz=metraz
        self.liczba_pokoi=liczba_pokoi

    def print_info(self):
        print(self.get_info())

    def get_info(self) -> str:
        return f"Ogloszenie ID: {self.id}, tytuł: {self.tytul}, opis: {self.opis}\n cena: {self.cena}, " \
               f"dane sprzedawcy: {self.dane_sprzedawcy}, {self.tel_kontakt}, {self.mail_kontakt}, " \
               f"{self.miejscowosc}, {self.metraz}m2, liczba pokoi: {self.liczba_pokoi}."

    def __str__(self):
        return self.get_info()

def test_ilosci_ogloszen():
    a = OgloszenieSamochodowe("Sprzedam", "Sprzedam samochod", 3000, "opo@opo.pl", "Adam Kowalski", "123-456-789",
                              "Nissan", "Primera", 1989, 100000, 2000, 100, "benzyna")
    b = OgloszenieMieszkaniowe("Sprzedam", "Sprzedam mieszkanie", 100000, "opo@opo.pl", "Adam Kowalski", "123-456-789",
                               "Warszawa", 45, 3)
    assert len(Ogloszenia.lista_id)==2

def test_poprawnosci_ogloszenia():
    c = OgloszenieSamochodowe("Sprzedam", "Sprzedam samochod", 3000, "opo@opo.pl", "Adam Kowalski", "123-456-789",
                              "Nissan", "Primera", 1989, 100000, 2000, 100, "benzyna")
    assert c.tytul=="Sprzedam" and c.opis=="Sprzedam samochod" and c.paliwo=="benzyna" and c.rok==1989