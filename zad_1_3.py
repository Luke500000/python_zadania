wzrost = float(input(f"Podaj wzrost w cm: "))
wzrost/=100
masa = float(input(f"Podaj masę w kg: "))
bmi = masa/(wzrost ** 2)
print(f"Twoje BMI wynosi: {bmi:.2f}")
print(f"Interpretacja:")
if bmi < 16:
    print(f"Wygłodzenie, rekomendowany przyrost masy ciała")
elif 16 <= bmi < 17:
    print(f"Wychudzenie, rekomendowany przyrost masy ciała")
elif 17 <= bmi < 18.5:
    print(f"Niedowaga, rekomendowany przyrost masy ciała")
elif 18.5 <= bmi < 25:
    print(f"Wartość prawidłowa, optymalna waga")
elif 25 <= bmi < 30:
    print(f"Nadwaga, rekomendowana redukcja masy ciała")
elif 30 <= bmi < 35:
    print(f"1. stopnień otyłości rekomendowana redukcja masy ciała")
elif 35 <= bmi < 40:
    print(f"2. stopnień otyłości rekomendowana redukcja masy ciała")
else:
    print(f"3. stopnień otyłości rekomendowana redukcja masy ciała")

