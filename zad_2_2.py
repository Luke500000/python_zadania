# Do przeróbki

liczba = int(input(f"Podaj liczbę choinek: "))
for x in range(0, liczba):
    napis=" * " * (x+1)
    b = 3 * liczba
    wart ='{:^'+ str(b) +'}'
    print(wart.format(napis))