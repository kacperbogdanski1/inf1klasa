a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("tak")
        else:
            print("nie")
    else:
        print("nie")
else:
    print("nie")


a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("trojkat rownoboczny")
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("trojkat rownoramienny prostokatny")
        else:
            print("trojkat rownoramienny")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("trojkat prostokatny roznoboczny")
    else:
        print("trojkat roznoboczny")
else:print("nie")




