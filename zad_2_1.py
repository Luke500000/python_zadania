### Zadanie 2.1 | Zagadka matematyczna

import random
liczba1 =random.randint(0,99)
liczba2 =random.randint(0,99)
print(f"Liczba1: {liczba1}")
print(f"Liczba2: {liczba2}")
suma = liczba1 + liczba2
suma_uzytk = int(input(f"Suma zdaniem użytkownika: "))
while suma_uzytk != suma:
    suma_uzytk = int(input(f"Suma zdaniem użytkownika: "))
print(f"Wszystko się zgadza, koniec programu.")
