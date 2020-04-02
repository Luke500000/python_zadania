import math

a = float(input(f"Podaj pierwszy bok trójkąta: "))
b = float(input(f"Podaj drugi bok trójkąta: "))
c = float(input(f"Podaj trzeci bok trójkąta: "))
if (a+b) > c and (b+c) > a and (a+c) > b:
    print(f"Trójkąt o podanych bokach istnieje.")
    obwod_polowa = (a + b + c) / 2
    pole = math.sqrt(obwod_polowa*(obwod_polowa-a)*(obwod_polowa-b)*(obwod_polowa-c))
    print(f"Pole trójkąta wynosi: {pole:.2f}.")
else:
    print(f"Trójkąt o podanych bokach nie istnieje.")