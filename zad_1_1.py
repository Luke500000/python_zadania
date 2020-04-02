#Pierwsza część zadania
cena_ziemniaki_kg = float(input("Podaj, ile kosztuje kg ziemniaków: "))
ilosc_kg = 5
cena_koncowa = cena_ziemniaki_kg*ilosc_kg
print(f"Cena kupna {ilosc_kg} kg ziemniaków wynosi: {cena_koncowa:.2f} zł.")

#Druga część zadania
cena_ziemniaki_kg = float(input("Podaj, ile kosztuje kg ziemniaków: "))
ilosc_kg = float(input("Podaj, ile kg ziemniaków chcesz kupić? "))
cena_koncowa = cena_ziemniaki_kg*ilosc_kg
print(f"Cena kupna {ilosc_kg} kg ziemniaków wynosi: {cena_koncowa:.2f} zł.")

#Trzecia część zadania
cena_ziemniaki_kg = float(input("Podaj, ile kosztuje kg ziemniaków: "))
ilosc_ziemniaki_kg = float(input("Podaj, ile kg ziemniaków chcesz kupić? "))
cena_banany_kg = float(input("Podaj, ile kosztuje kg bananow: "))
ilosc_banany_kg = float(input("Podaj, ile kg bananów chcesz kupić? "))
cena_banany_koncowa = cena_banany_kg*ilosc_banany_kg
cena_ziemniaki_koncowa = cena_ziemniaki_kg*ilosc_ziemniaki_kg
koszt_calk=cena_banany_koncowa + cena_ziemniaki_koncowa
print(f"Cena bananów: {cena_banany_koncowa:.2f} zł, Cena ziemniaków: {cena_ziemniaki_koncowa:.2f} zł.")
print(f"Cena całkowita: {koszt_calk:.2f} zł.")
if cena_banany_koncowa > cena_ziemniaki_koncowa:
    print(f"Banany kosztują więcej.")
elif cena_banany_koncowa < cena_ziemniaki_koncowa:
    print(f"Ziemniaki kosztują więcej.")
else:
    print(f"Ziemniaki i banany kosztują tyle samo.")