print("Введите число и его степень через пробел")
a, b = input().split(' ')
a = float(a) 
b = float(b)

def pow(x, y, f = True):  
    if f:
        if y == 0:
            return 1
        elif y < 0:
            x = 1/x
        elif x == 1 or x == 0:
            return x

    if y >= -1 and y <= 1:
        return x
    elif y > 1:
        return x * pow(x, y - 1, False)
    elif y < -1:
        return x * pow(x, y + 1, False)

print(pow(a,b))