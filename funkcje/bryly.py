import math

def obj_szescianu(a: float) -> float:
    return a ** 3

def pp_szescianu(a: float) -> float:
    return 6 * (a ** 2)

# ------------------------------------------------------------------------------
def obj_prostopadloscianu(a: float, b: float, h: float) -> float:
    return a * b * h

def pp_prostopadloscianu(a: float, b: float, h: float) -> float:
    return 2 * (a * b + a * h + b * h)

# ------------------------------------------------------------------------------
def obj_waleca(r: float, h: float) -> float:
    return math.pi * (r ** 2) * h

def pp_waleca(r: float, h: float) -> float:
    return 2 * math.pi * r * (r + h)

# ------------------------------------------------------------------------------
def legenda_bryl() -> None:
    print("a -- szescian (objetosc i pole)")
    print("b -- prostopadloscian (objetosc i pole)")
    print("c -- walec (objetosc i pole)")
    print("e -- Exit")

def jakie_bryly() -> None:
    while True:
        legenda_bryl()
        inp = input().lower().strip()
        if inp == "e":
            print("Exit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla a = {a} -> objetosc = {obj_szescianu(a)}, pole calkowite = {pp_szescianu(a)}")
        elif inp == "b": 
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"dla a = {a}, b = {b}, h = {h} -> objetosc = {obj_prostopadloscianu(a, b, h)}, pole calkowite = {pp_prostopadloscianu(a, b, h)}")
        elif inp == "c":
            r = float(input("r (plomien/promien) = "))
            h = float(input("h (wysokosc) = "))
            print(f"dla r = {r}, h = {h} -> objetosc = {obj_waleca(r, h):.2f}, pole calkowite = {pp_waleca(r, h):.2f}")


if __name__ == "__main__":
    jakie_bryly()