print("Введите объем первого вещества")
a = float(input())
print("Введите массу первого вещества")
b = float(input())
print("Введите объем второго вещества")
c = float(input())
print("Введите массу второго вещества")
d = float(input())
e = b / a
f = d / c
if e > f:
    print("Плотность первого материала больше")
elif e < f:
    print("Плотность второго материала больше")
else:
    print("Плотности материалов равны")