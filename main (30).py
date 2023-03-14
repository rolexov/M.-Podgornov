a=int(input("Прилежащий катет"))
b-int(input("Противолежащий катет"))
с=int(input("гипотенуза"))
if c**2==a**2+b**2:
    sin=b/c
    cos=a/c
    p=3.14
    if sin<= p/4:
        print(sin)
        elif cos>p/4:
            print(cos)
            else:print("прилежащий больше противолежащего")
            else:print("прямоугольного треугольника не существует")