"""### Zadanie 4.2 | Lista ogłoszeń
​
Napisz programy, w których tworzysz listę ogłoszeń samochodowych,
a następnie wyszukujesz ogłoszenia na podstawie ich parametrów.
Na przykład ogłoszenia o cenach z określonego przedziału.
​
Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać
wyszukane. Użyj poznanych kolekcji do trzymania ogłoszeń.
Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń
"""
import random

class Samochod:
    #listy z parametrami aut
    marka = list(["Opel", "Nissan", "Honda", "Fiat", "BMW", "Tesla"])
    opel = list(["Corsa", "Astra", "Insignia"])
    nissan = list(["Primera", "Almera", "Juke"])
    honda = list(["Accord", "Jazz", "Civic"])
    fiat = list(["Punto", "Uno", "500"])
    bmw = list(["I8", "E4", "E5"])
    tesla = list(["3", "S", "X"])
    lista_paliwo = list(["benzyna", "diesel", "hybryda"])

    lista_id=set() #lista do przechowywania id
    slownik=dict() #slownik z wszystkimi ogłoszeniami

    def __init__(self):
        self.marka=self.przydziel_marke()
        self.model=self.przydziel_model()
        self.rok_produkcji=self.przydziel_rok()
        self.paliwo=self.przydziel_paliwo()
        self.stan=self.przydziel_stan()
        self.przebieg=self.przydziel_przebieg()
        self.cena=self.przydziel_cene()
        self.id=self.przydziel_id(Samochod.lista_id)
        Samochod.slownik[self.id]=[self.marka, self.model, self.rok_produkcji, self.paliwo, self.stan, self.przebieg, self.cena]

    def przydziel_marke(self):
        return random.choice(Samochod.marka)

    def przydziel_model(self):
        if self.marka == "Opel":
            return random.choice(Samochod.opel)
        elif self.marka == "Nissan":
            return random.choice(Samochod.nissan)
        elif self.marka == "Honda":
            return random.choice(Samochod.honda)
        elif self.marka == "Fiat":
            return random.choice(Samochod.fiat)
        elif self.marka == "BMW":
            return random.choice(Samochod.bmw)
        elif self.marka == "Tesla":
            return random.choice(Samochod.tesla)
        else:
            return "Nieznany"

    def przydziel_rok(self):
        return random.randint(1980,2020)

    def przydziel_paliwo(self):
        if self.marka == "Tesla":
            return "elektryczny"
        else:
            return random.choice(Samochod.lista_paliwo)

    def przydziel_stan(self):
        if self.rok_produkcji == 2020:
            return "nowy"
        else:
            return "używany"

    def przydziel_przebieg(self):
        if self.rok_produkcji == 2020:
            return 0
        else:
            return random.randint(1, 500000)

    def przydziel_cene(self):
        return random.randint(1000, 50000)

    def przydziel_id(self,lista_id:list):
        liczba = random.randint(1, 1000000000)
        while liczba in lista_id:
            liczba = random.randint(1, 1000000000)
        lista_id.add(liczba)
        return liczba

    def print_info(self):
        print(self.get_info())

    def get_info(self) -> str:
        return f"Ogloszenie ID: {self.id}, marka: {self.marka}, model: {self.model}, rok_prod: {self.rok_produkcji}\n " \
               f"cena: {self.cena} PLN, {self.paliwo}, {self.stan}, {self.przebieg} km"

    def __str__(self) -> str:
        return self.get_info()

#Automatyczne tworzenie ogłoszeń
a = Samochod()
b = Samochod()
c = Samochod()
d = Samochod()
print(a)
print(b)
print(c)
print(d)

#parametr=int(input("Podaj cenę minimalną: ")) #cena minimalna
parametr=1000

#Metoda 1 - użycie for + if
print("Metoda 1")
print(f"Ceny większe od {parametr}:")
for klucz, wartosc in Samochod.slownik.items():
    if wartosc[6]>parametr:
        print(f"ID: {klucz}, cena: {wartosc[6]}")

#Metoda 2 - użycie funkcja anonimowa lambda + filter
print("Metoda 2")
klucze=[klucz for klucz, wartosc in Samochod.slownik.items()]
wartosci=[wartosc[6] for klucz, wartosc in Samochod.slownik.items()]
przefiltrowane = list(filter(lambda cena: cena>parametr, wartosci))
print(przefiltrowane)

def test_ilosci_ogloszen():
    assert len(Samochod.lista_id)==4