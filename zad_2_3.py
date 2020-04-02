ile = int(input(f"Ile liczb? "))
suma = 0
for x in range(0, ile):
    liczba=float(input(f"Nr liczby {x+1}, podaj liczbę: "))
    suma+=liczba
    if x == 0:
        min = liczba
        max = liczba
    else:
        if liczba <= min:
            min = liczba
        if liczba >= max:
            max = liczba
srednia = suma / ile
print(f"Suma: {suma:.2f}, srednia: {srednia:.2f}, min.: {min}, max.: {max}.")



