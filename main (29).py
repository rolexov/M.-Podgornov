print("a указано в м/с")
print("b указано в км/ч")
a,b=int(input()),int(input())
x = b / 3.6
if a > x:
    print("Значение a больше значения b")
elif a < x:
    print("Значение b больше значения a")
else:
    print(a=b)
    