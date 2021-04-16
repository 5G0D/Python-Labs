print ("Введите число")
n = int(input())

num = 1
power = 1
while num <= n:
    power += 1
    num *= 2
power -= 1

print(power)
