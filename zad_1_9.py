### Zadanie 1.9 FizzBuzz

licznik = 0
while licznik < 100:
    licznik+=1
    print(licznik, end=" ")
    if licznik % 3 == 0:
        print("Fizz", end="")
    if licznik % 5 == 0:
        print("Buzz", end="")
    print()