# 1.Napisz program który przyjmie od użytkownika r i policzy V kuli.
# def obietosc_kuli(r):
#     import math 
#     wynik = (4/3) * math.pi * r**3
#     return wynik  
# r = float(input("Podaj promień kuli: "))
# print(obietosc_kuli(r))


# 2.Napisz program który wyświetli n razy kocham programować.
# n = int(input("Podaj liczbę powtórzeń: "))
# for _ in range(n):
#     print("Kocham programować!")

# 3.Napisz program który sumuje liczby aż nie napisze się stop.

# n = 0

# while True:
#     wej = input("Podaj liczbę : ")
   
#     if wej.lower() == "stop":
#         break
        
#     try:
#         # Próbujemy zamienić wpisany tekst na liczbę i dodać do sumy
#         z = float(wej)
#         n += z
#     except ValueError:
#         print("To nie jest liczba. Spróbuj ponownie.")
# print(f" Suma podanych liczb wynosi: {n}")






# 4.Napisz program który policzy średnią arytmetyczną. Program przyjmuje liczby od użytkownika
# aż użytkownik nie wprowadzi słowa stop.






# 5a.Zsumuj n potęg liczby 2.
# Np: n =3
# 2^0+2^1+2^2 = 7




#1. Utwórz pustą listę o nazwie "numbers".
#numbers = []








# Oblicz sumę liczb znajdujących się w liście "numbers".

numbers = [0,1,2,3,3]


suma = 0
i = 0
while i < len(numbers):
     suma += numbers[i]
     i += 1
print(f"{numbers} - suma = {suma}")











#Znajdź średnią arytmetyczną liczb w liście "numbers".
