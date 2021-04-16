a = int(input("Введите число: "))
counter = 0

for i in range(2, a // 2 + 1):
    if (a % i == 0):
        counter += 1
if (counter <= 0):
    print("Число простое")
else:
    print("Число сложное")
