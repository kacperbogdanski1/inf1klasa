# 1.Wygeneruj tablice zawierającą n losowych elementów. Z zakresem min i max.
import random

n = 5  
minimum = 1
maksimum = 10

tablica = []
for i in range(n):
  tablica.append(random.randint(minimum, maksimum))

print("Wylosowana tablica:", tablica)

# 2.Napisz program(nie max min) znajdujący max i min wartość. tablica zawiera 1,1,1,5,5,-2,10,1

tablica = [1, 1, 1, 5, 5, -2, 10, 1]

minimum = tablica[0]
maksimum = tablica[0]

for element in tablica:
  if element < minimum:
    minimum = element
  if element > maksimum:
    maksimum = element

print("Najmniejsza wartość:", minimum)
print("Największa wartość:", maksimum)

# 3.Napisz program który powie ile razy powtórzył się n element na tablicy.


tablica = [1, 1, 1, 5, 5, -2, 10, 1]
n = 1  

licznik = 0
for element in tablica:
  if element == n:
    licznik += 1

print(f"Liczba {n} powtórzyła się {licznik} razy.")


# 4.Sprawdź ile liczb podzielnych przez n zawiera ta tablica.


tablica = [1, 2, 3, 4, 5, 6, 10]
n = 2  

licznik = 0
for element in tablica:
  if element % n == 0: 
    licznik += 1

print(f"W tablicy jest {licznik} liczb podzielnych przez {n}.")

# 5.Przepisz wszystkie elementy mniejsze od n do 2 tablicy wyświetl tą tablice.

tablica = [1, 5, -2, 10, 3]
n = 4

druga_tablica = []
for element in tablica:
  if element < n:
    druga_tablica.append(element)

print("Druga tablica (mniejsze od n):", druga_tablica)

# 6.Przyjmij n liczb od użytkownika sprawdź ile z wprowadzonych liczb jest parzystych. Zapisz
# liczby parzyste na nowej liście.

n = int(input("Ile liczb chcesz podać? "))
parzyste = []

for i in range(n):
  liczba = int(input(f"Podaj liczbę {i+1}: "))
  if liczba % 2 == 0:  
    parzyste.append(liczba)

print("Wprowadzone liczby parzyste to:", parzyste)

# 1.Masz tablice A przepisz do 2 tablice liczby podzielne przez 7.
tablica_a = [14, 5, 21, 8, 35, 10]
tablica_b = []

for liczba in tablica_a:
  if liczba % 7 == 0:  
    tablica_b.append(liczba)

print("Druga tablica (podzielne przez 7):", tablica_b)


# 2. Zsumuj liczby z tablicy, które są podzielne przez a.
tablica = [2, 4, 6, 8, 10, 12]
a = 3
suma = 0

for liczba in tablica:
  if liczba % a == 0:
    suma += liczba

print(f"Suma liczb podzielnych przez {a} wynosi:", suma)

# 3.Ile raz powtarza się x element w talicy.

tablica = [1, 5, 2, 5, 3, 5, 4]
x = 5

licznik = 0
for element in tablica:
  if element == x:
    licznik += 1

print(f"Element {x} powtórzył się {licznik} razy.")

# 4.Pod jakimi indeksami znajdują się minimalne wartości.
tablica = [5, 2, 9, 2, 7, 2]


minimum = tablica[0]
for element in tablica:
  if element < minimum:
    minimum = element


indeksy = []
for i in range(len(tablica)):
  if tablica[i] == minimum:
    indeksy.append(i)

print(f"Wartość minimalna to {minimum}, a jej indeksy to: {indeksy}")

# 5.Policz średnią harmoniczną.

tablica = [2, 3, 6]
n = len(tablica)

suma_odwrotnosci = 0
for element in tablica:
  suma_odwrotnosci += 1 / element

srednia_harmoniczna = n / suma_odwrotnosci

print("Średnia harmoniczna wynosi:", srednia_harmoniczna)

# 6.Przepisz do 2 tablicy liczby, z których pierwiastek jest liczbą całkowitą.

tablica = [4, 5, 9, 16, 20, 25]
druga_tablica = []

for liczba in tablica:
  if liczba >= 0:
    pierwiastek = liczba**0.5
    if int(pierwiastek) ** 2 == liczba:
      druga_tablica.append(liczba)

print("Liczby, których pierwiastek jest całkowity:", druga_tablica)
# 1.Tablica AAA zawiera 2,3,4,5,6,7,8,9,10,11,12,13
AAA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("Tablica AAA:", AAA)

# 2.Policz średnią harmoniczną powyższej tablicy.
AAA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
n = len(AAA)

suma_odwrotnosci = 0
for element in AAA:
  suma_odwrotnosci += 1 / element

srednia_harmoniczna = n / suma_odwrotnosci
print("Średnia harmoniczna tablicy AAA wynosi:", srednia_harmoniczna)

# 3.Przepisz wszystkie liczby nieparzyste to 2 tablicy. Wyświetl je w jednej linijce.
AAA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
druga_tablica = []
for element in AAA:
  if element % 2 != 0:  
    druga_tablica.append(element)
print("Liczby nieparzyste:", *druga_tablica)
# 4.Odcinek o długości n podziel na 3 losowe wartości. Napisz kod co sprawdzi czy podział został
# dokonany poprawnie.

import random

n = 15  

p1 = random.uniform(0, n)
p2 = random.uniform(0, n)

punkt1 = min(p1, p2)
punkt2 = max(p1, p2)

czesc1 = punkt1
czesc2 = punkt2 - punkt1
czesc3 = n - punkt2

suma_czesci = czesc1 + czesc2 + czesc3

poprawnie = abs(suma_czesci - n) < 0.00001

print(f"Części odcinka: {czesc1:.2f}, {czesc2:.2f}, {czesc3:.2f}")
print(f"Suma części: {suma_czesci:.2f}")
print("Czy podział został dokonany poprawnie?", poprawnie)
# 5.Wyświetl pod jakimi indeksami znajduje się n element.
tablica = [2, 5, 3, 5, 7, 5, 8]
n = 5  
indeksy = []
for i in range(len(tablica)):
  if tablica[i] == n:
    indeksy.append(i)

print(f"Element {n} znajduje się pod indeksami:", indeksy)

# 6.Powiedz ile liczb pierwszych zawiera tablica
AAA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

licznik_pierwszych = 0

for liczba in AAA:
  if liczba < 2:
    continue 

  czy_pierwsza = True
  for i in range(2, int(liczba**0.5) + 1):
    if liczba % i == 0:
      czy_pierwsza = False
      break

  if czy_pierwsza:
    licznik_pierwszych += 1

print(f"W tablicy znajduje się {licznik_pierwszych} liczb pierwszych.")