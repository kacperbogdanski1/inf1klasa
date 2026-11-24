import math

# ------------------------------------------------------------------------------
# SZESCIAN
def obj_szescianu(a: float) -> float:
    return a ** 3

def pp_szescianu(a: float) -> float:
    return 6 * (a ** 2)

# ------------------------------------------------------------------------------
# PROSTOPADLOSCIAN
def obj_prostopadloscianu(a: float, b: float, h: float) -> float:
    return a * b * h

def pp_prostopadloscianu(a: float, b: float, h: float) -> float:
    return 2 * (a * b + a * h + b * h)

# ------------------------------------------------------------------------------
# WALEC
def obj_waleca(r: float, h: float) -> float:
    return math.pi * (r ** 2) * h

def pp_waleca(r: float, h: float) -> float:
    return 2 * math.pi * r * (r + h)

# ------------------------------------------------------------------------------
def legenda_bryl() -> None:
    print("\na -- szescian (objetosc i pole)")
    print("b -- prostopadloscian (objetosc i pole)")
    print("c -- walec (objetosc i pole)")
    print("e -- Exit")

def jakie_bryly() -> None:
    while True:
        legenda_bryl()
        inp = input("Wybierz opcje: ").lower().strip()
        
        if inp == "e":
            print("Exit")
            break
            
        elif inp == "a":
            a_tekst = input("a = ")
            if not a_tekst.isdigit():
                print("Blad: to nie jest liczba!")
            else:
                a = float(a_tekst)
                if a <= 0:
                    print("Blad: bok musi byc wiekszy od zera!")
                else:
                    print(f"dla a = {a} -> objetosc = {obj_szescianu(a)}, pole calkowite = {pp_szescianu(a)}")
                
        elif inp == "b": 
            a_tekst = input("a = ")
            b_tekst = input("b = ")
            h_tekst = input("h = ")
            if not (a_tekst.isdigit() and b_tekst.isdigit() and h_tekst.isdigit()):
                print("Blad: wszystkie wartosci musza byc liczbami!")
            else:
                a = float(a_tekst)
                b = float(b_tekst)
                h = float(h_tekst)
                if a <= 0 or b <= 0 or h <= 0:
                    print("Blad: wszystkie boki i wysokosc musza byc wieksze od zera!")
                else:
                    print(f"dla a = {a}, b = {b}, h = {h} -> objetosc = {obj_prostopadloscianu(a, b, h)}, pole calkowite = {pp_prostopadloscianu(a, b, h)}")
                
        elif inp == "c":
            r_tekst = input("r (promien) = ")
            h_tekst = input("h (wysokosc) = ")
            if not (r_tekst.isdigit() and h_tekst.isdigit()):
                print("Blad: promien i wysokosc musza byc liczbami!")
            else:
                r = float(r_tekst)
                h = float(h_tekst)
                if r <= 0 or h <= 0:
                    print("Blad: promien i wysokosc musza byc wieksze od zera!")
                else:
                    print(f"dla r = {r}, h = {h} -> objetosc = {obj_waleca(r, h):.2f}, pole calkowite = {pp_waleca(r, h):.2f}")
                
        else:
            print("Nieznana komenda, sprobuj ponownie.")


if __name__ == "__main__":
    jakie_bryly()