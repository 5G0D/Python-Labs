print ("Введите число")
a = int(input())

def fact(n):
    if n > 1:
        return n*fact(n-1)
    else:
        return n

print(fact(a))