print('Введите числа и действие через пробел')
x,f,y = input().split(' ')
x = int(x)
y = int(y)

calc = {
    '/': x/y,
    '*': x*y,
    '+': x+y,
    '-': x-y
}

print(calc.get(f, 'Ошибка'))
