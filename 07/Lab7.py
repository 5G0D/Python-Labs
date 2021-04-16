import math as m
f = int(input("Выберете способ решения (1/2): "))            

if (f == 1):
    a = int(input("Введите 1 сторону: "))
    b = int(input("Введите 2 сторону: "))
    c = int(input("Введите 3 сторону: "))
    if ((a < b + c) & (b < a + c) & (c < a + b)):
        p = (a + b + c) / 2
        S = m.sqrt(p * (p - a) * (p - b) * (p - c))
        print("S =", S)
    else:
        print("Такой треугольник не может существовать!")
elif (f == 2):
    x1 = int(input("Введите x1: "))
    y1 = int(input("Введите y1: "))
    x2 = int(input("Введите x2: "))
    y2 = int(input("Введите y2: "))
    x3 = int(input("Введите x3: "))
    y3 = int(input("Введите y3: "))
    a = m.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
    b = m.sqrt(((x3 - x2) * (x3 - x2)) + ((y3 - y2) * (y3 - y2)))
    c = m.sqrt(((x3 - x1) * (x3 - x1)) + ((y3 - y1) * (y3 - y1)))
    if ((a < b + c) & (b < a + c) & (c < a + b)):
        p = (a + b + c) / 2
        S = m.sqrt(p * (p - a) * (p - b) * (p - c))
        print("S =", S)
    else:
        print("Такой треугольник не может существовать!")
else:
     print("Ошибочный ввод")   


    
