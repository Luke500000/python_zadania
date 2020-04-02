### Zadanie 2.4 | Zgadnij liczbę z zakresu

import random
liczba=random.randint(0,999)
krok=0
#print(f"Wylosowana liczba: {liczba}")
while True:
    krok+=1
    wart = int(input(f"Podaj liczbę: "))
    if wart > liczba:
        print(f"Wartośc zbyt duża.")
    elif wart < liczba:
        print(f"Wartośc za mała.")
    elif wart == liczba:
        print(f"Brawo udało Ci się zgadnąć w {krok} kroku.")
        exit()

