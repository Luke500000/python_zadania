### Zadanie 1.9 FizzBuzz

licznik = 0
while licznik < 100:
    licznik+=1
    if licznik % 3 == 0:
        print("Fizz", end="")
    elif licznik % 5 == 0:
        print("Buzz", end="")
    else:
        print(licznik, end=" ")
    print()