import math as m
print('Введите x0')
x0 = int(input())
print("Введите v0")
v0 = int(input())
print("Введите t")
t = int(input())
g = 9.8
print("x("+str(t)+") =", m.fabs((x0+v0*t-(g*t*t)/2)-x0))
