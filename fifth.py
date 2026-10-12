#  1. Utwórz pustą listę o nazwie "numbers".
# print("1-=-"*10)
# numbers = []
# print(len(numbers))


# print(numbers)


#  2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.

# print("2-=-"*10)
# print(numbers)


# i = 0
# while i < 5:
#     inp = float(input())
#     numbers.append(inp)
#     print(numbers)
#     i += 1





#  3. Oblicz sumę liczb znajdujących się w liście "numbers".

# print("3-=-"*10)
# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# print(numbers)




# suma = 0
# i = 0
# while i < len(numbers):
#     suma += numbers[i]
#     i += 1
# print(f"{numbers} - suma = {suma}")






#  4. Znajdź największą liczbę w liście "numbers".

# print("4-=-"*10)
# numbers = [0,1,2,3,4,5,6,7,8,9,10]




# my_max = numbers[0]
# i = 0
# while i < len(numbers):
#     if my_max < numbers[i]:
#         my_max = numbers[i]
#     i += 1
# print(f"my_max = {my_max}")





#  5. Znajdź najmniejszą liczbę w liście "numbers".
# print("5-=-"*10)
# numbers = [0,1,2,3,4,5,6,7,8,9,10]




# my_min = numbers[0]
# i = 0
# while i < len(numbers):
#     if my_min > numbers[i]:
#         my_min = numbers[i]
#     i += 1
# print(f"my_max = {my_min}")






#  6. Znajdź średnią arytmetyczną liczb w liście "numbers".
# print("6-=-"*10)
# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# print(numbers)




# my_sum = 0
# i = 0
# while i < len(numbers):
#     my_sum += numbers[i]
#     i += 1
# print(my_sum/len(numbers))




#  7. Znajdź ilość liczb parzystych w liście "numbers".

# print("7-=-"*10)
# numbers = [0,1,2,3,4,5,6,7,8,9,10]




# i = 0
# parzyste = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#          parzyste += 1

#  8. Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".
# numbers = [0,1,2,3,4,5,6,7,8,9,10,0,1,2,3,4,5,6,7,8,9,10]
# duplicates = []
# i = 0


# while i < len(numbers):
#     if numbers.count(numbers[i]) > 1 and numbers[i] not in duplicates:
#         duplicates.append(numbers[i])
#     i += 1
# print(numbers)
# print(duplicates)



#  9. Usuń wszystkie powtarzające się elementy z listy "numbers".
# print("9-=-"*10)
# numbers = [1,1,1,2,2,5,5,5]
# new_list = []




# i = 0
# while i < len(numbers):
#     if numbers[i] not in new_list:
#         new_list.append(numbers[i])
#     i += 1


# print(new_list)



#  10. Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".
# print("9-=-"*10)
# numbers = [1,1,1,2,2,5]
# squares = []
# i = 0
# while i < len(numbers):
#     squares.append(numbers[i]**2)
# print(numbers)



# 1. Napisz program, który poprosi użytkownika o wprowadzenie liczby i sprawdzi, czy jest dodatnia, ujemna czy równa zero. Wyświetl odpowiedni komunikat.

liczba = float(input("Podaj liczbę: "))


if liczba > 0:
    print("Liczba jest dodatnia.")
elif liczba < 0:
    print("Liczba jest ujemna.")
else:
    print("Liczba jest równa zero.")





# 2. Poproś użytkownika o podanie swojego wieku. Jeśli wiek jest większy lub równy 18, wyświetl komunikat "Jesteś pełnoletni". W przeciwnym razie wyświetl komunikat "Jesteś niepełnoletni".

wiek = int(input("Podaj swój wiek: "))


if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    print("Jesteś niepełnoletni.")



# 3. Poproś użytkownika o wprowadzenie dwóch liczb. Sprawdź, która liczba jest większa i wyświetl odpowiedni komunikat.
n1 = float(input("Podaj pierwszą liczbę: "))
n2 = float(input("Podaj drugą liczbę: "))


if n1 > n2:
    print("Pierwsza liczba jest większa od drugiej.")
elif n1 < n2:
    print("Druga liczba jest większa od pierwszej.")
else:
    print("Obie liczby są równe.")




# 4. Stwórz listę liczb i sprawdź, czy dana liczba jest w tej liście. Wyświetl odpowiedni komunikat.

ocena = float(input("Podaj ocenę: "))


if ocena >= 4:
    print("Zaliczone.")
else:
    print("Niezaliczone.")


# 5. Poproś użytkownika o podanie oceny szkolnej. Jeśli ocena jest większa lub równa 4, wyświetl komunikat "Zaliczone". W przeciwnym razie wyświetl komunikat "Niezaliczone".
rok = int(input("Podaj rok: "))


if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print(rok, "jest rokiem przestępnym.")
else:
    print(rok, "nie jest rokiem przestępnym.")



# 6. Napisz program, który poprosi użytkownika o wprowadzenie roku. Sprawdź, czy podany rok jest rokiem przestępnym. Wyświetl odpowiedni komunikat.
liczba = int(input("Podaj liczbę: "))


if liczba % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")



# 7. Poproś użytkownika o podanie liczby. Sprawdź, czy liczba jest parzysta czy nieparzysta. Wyświetla odpowiedni komunikat.
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))


if a + b > c and b + c > a and c + a > b:
    print("Można zbudować trójkąt.")
else:
    print("Nie można zbudować trójkąta.")



# 8. Napisz program, który sprawdzi, czy podane trzy liczby mogą być bokami trójkąta. Wyświetla odpowiedni komunikat.
liczba = int(input("Podaj liczbę: "))


if liczba % 3 == 0 and liczba % 5 == 0:
    print("Liczba jest podzielna przez 3 i 5.")
else:
    print("Liczba nie jest podzielna przez 3 i 5.")



# 9. Poproś użytkownika o podanie liczby. Sprawdź, czy liczba jest podzielna przez 3 i 5 jednocześnie. Wyświetl odpowiedni komunikat.


# 1.Wyświetl wszystkie liczby z listy "numbers" w odwrotnej kolejności.
print("9-=-"*10)
numbers = [1,1,1,2,2,5]


i = -1
while i >= -len(numbers):
    print(numbers[i])
    i-= 1


# 2.Poproś użytkownika o podanie liczby. Sprawdź, czy liczba ta znajduje się w liście "numbers". Wyświetl odpowiedni komunikat.
print("9-=-"*10)
numbers = [1,1,1,2,2,5]
inp = int(input())
if inp in numbers:
    print("Tak")
else:
    print("Nie")




# 3.Wyświetl indeks pierwszego wystąpienia danej liczby w liście "numbers".
print("9-=-"*10)
numbers = [1,1,1,2,2,5]
inp = int(input())
i = 0
while i < len(numbers):
    if inp == numbers[i]:
        print(i)
        break
    i += 1



# 4.Znajdź ilość liczb większych niż 10 w liście "numbers".

print("9-=-"*10)
numbers = [1,1,1,2,2,5,11]
ile = 0
i = 0
while i < len(numbers):
    if numbers[i] > 10:
        ile += 1
    i += 1
print(ile)


# 5.Posortuj listę "numbers" w kolejności malejącej.
print("9-=-"*10)
numbers = [11,2,10,3,1,2,4]
numbers.sort(reverse=True)
print(numbers)


# 6.Znajdź drugą największą liczbę w liście "numbers".


print("9-=-"*10)
numbers = [11,2,10,3,1,2,4,11]


max1 = float('-inf')
max2 = float('-inf')


i = 0
while i < len(numbers):
    if numbers[i] > max1:
        max2 = max1
        max1 = numbers[i]
    elif numbers[i] > max2 and numbers[i] != max1:
        max2 = numbers[i]
    i += 1


print(f"max1 {max1}")
print(f"max2 {max2}")




# 7.Stwórz nową listę o nazwie "doubled_numbers" zawierającą podwojoną wartość każdej liczby z listy "numbers".
print("9-=-"*10)
numbers = [1,1,2,2,3,3,4,4,10,10,10,10]
doubled_numbers = []


i = 0
while i < len(numbers):
    doubled_numbers.append(numbers[i]*2)
    i += 1
print(doubled_numbers)    




# 8.Zlicz ilość wystąpień danej liczby w liście "numbers".
print("9-=-"*10)
numbers = [1,1,2,2,3,3,4,4,10,10,10,10]
i = 0
inp = float(input("-"))
ile = 0
while i < len(numbers):
    if numbers[i] == inp:
        ile += 1
    i += 1
print(ile)


# 9.Wyświetl wszystkie liczby z listy "numbers" z ich indeksami.

print("9-=-"*10)
numbers = [1,1,2,2,3,3,4,4,10,10,10,10]


i = 0
while i < len(numbers):
    print(f"{i} {numbers[i]}")
    i += 1




