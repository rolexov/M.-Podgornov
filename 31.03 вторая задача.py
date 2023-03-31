a=int(input("пробег"))
b=int(input("день"))
x=a%10
x1=a//10%10
x2=a//100%10
if (x+x1+x2)>b:
    b*0
    print("сброс")
else: print("Сегодня не сломается"+ str(a))
