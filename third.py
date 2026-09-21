import math

print("Bryly - a | Plaskie - b")
inp = input("inp: ").lower().strip()

if inp == "a":
    print("ppBryl - a | vBryl - b")
    inp = input("inp: ").lower().strip()
    
    if inp == "a":
        print("ppSzescianu - a | ppProstopadloscianu - b | ppGraniastoslupa - c | ppOstroslupa - d | ppWalca - e | ppStozka - f | ppKuli - g")
        inp = input("inp: ").lower().strip()
        
        if inp == "a":
            a = float(input("a = "))
            print(f"ppSzescianu o boku {a} = {6 * a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"ppProstopadloscianu o bokach {a}, {b}, {c} = {2*a*b + 2*b*c + 2*c*a}")
        elif inp == "c":
            pp = float(input("Pp = "))
            pb = float(input("Pb = "))
            print(f"ppGraniastoslupa = {2 * pp + pb}")
        elif inp == "d":
            pp = float(input("Pp = "))
            pb = float(input("Pb = "))
            print(f"ppOstroslupa = {pp + pb}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("H = "))
            print(f"ppWalca = {2 * math.pi * r**2 + 2 * math.pi * r * h}")
        elif inp == "f":
            r = float(input("r = "))
            l = float(input("l = "))
            print(f"ppStozka = {math.pi * r**2 + math.pi * r * l}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"ppKuli = {4 * math.pi * r**2}")
        else:
            print("Nie ma takiej komendy")

    elif inp == "b":
        print("vSzescianu - a | vProstopadloscianu - b | vGraniastoslupa - c | vOstroslupa - d | vWalca - e | vStozka - f | vKuli - g")
        inp = input("inp: ").lower().strip()
        
        if inp == "a":
            a = float(input("a = "))
            print(f"vSzescianu = {a**3}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"vProstopadloscianu = {a * b * c}")
        elif inp == "c":
            pp = float(input("Pp = "))
            h = float(input("H = "))
            print(f"vGraniastoslupa = {pp * h}")
        elif inp == "d":
            pp = float(input("Pp = "))
            h = float(input("H = "))
            print(f"vOstroslupa = {(1/3) * pp * h}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("H = "))
            print(f"vWalca = {math.pi * r**2 * h}")
        elif inp == "f":
            r = float(input("r = "))
            h = float(input("H = "))
            print(f"vStozka = {(1/3) * math.pi * r**2 * h}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"vKuli = {(4/3) * math.pi * r**3}")
        else:
            print("Nie ma takiej komendy")
    else:
        print("Nie ma takiej komendy")

elif inp == "b":
    print("obwody fig plaskich - a | pole fig plaskich - b | inne wzory plaskie - c")
    inp = input("inp: ").lower().strip()
    
    if inp == "a":
        print("obwKwadratu - a | obwProstokata - b | obwRownolegloboku - c | obwTrapezu - d | obwTrojkata - e | obwTrojkataRownobocznego - f | obwKola - g | obwRombu - h")
        inp = input("inp: ").lower().strip()
        
        if inp == "a":
            a = float(input("a = "))
            print(f"obwKwadratu = {4 * a}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"obwProstokata = {2 * a + 2 * b}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"obwRownolegloboku = {2 * a + 2 * b}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"obwTrapezu = {a + b + c + d}")
        elif inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"obwTrojkata = {a + b + c}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"obwTrojkataRownobocznego = {3 * a}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"obwKola = {2 * math.pi * r}")
        elif inp == "h":
            a = float(input("a = "))
            print(f"obwRombu = {4 * a}")
        else:
            print("Nie ma takiej komendy")

    elif inp == "b":
        print("pKwadratu - a | pProstokata - b | pRownolegloboku - c | pTrapezu - d | pTrojkata - e | pTrojkataRownobocznego - f | pKola - g | pRombu(z h) - h | pRombu(z e,f) - i")
        inp = input("inp: ").lower().strip()
        
        if inp == "a":
            a = float(input("a = "))
            print(f"pKwadratu = {a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"pProstokata = {a * b}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pRownolegloboku = {a * h}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"pTrapezu = {((a + b) * h) / 2}")
        elif inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pTrojkata = {0.5 * a * h}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"pTrojkataRownobocznego = {(a**2 * math.sqrt(3)) / 4}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"pKola = {math.pi * r**2}")
        elif inp == "h":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pRombu = {a * h}")
        elif inp == "i":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"pRombu = {(e * f) / 2}")
        else:
            print("Nie ma takiej komendy")

    elif inp == "c":
        print("hTrojkataRownobocznego - a | przekatnaKwadratu - b | twierdzeniePitagorasa - c")
        inp = input("inp: ").lower().strip()
        
        if inp == "a":
            a = float(input("a = "))
            print(f"hTrojkataRownobocznego = {(a * math.sqrt(3)) / 2}")
        elif inp == "b":
            a = float(input("a = "))
            print(f"przekatnaKwadratu = {a * math.sqrt(2)}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"przeciwprostokatna c = {math.sqrt(a**2 + b**2)}")
        else:
            print("Nie ma takiej komendy")

    else:
        print("Nie ma takiej komendy")

else:
    print("Nie ma takiej komendy")
























































































































































