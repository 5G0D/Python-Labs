from random import randint
import math as m

def is_sorted(l, reverse=False):
    if reverse:
        return all(a >= b for a, b in zip(l, l[1:]))
    else:
        return all(a <= b for a, b in zip(l, l[1:]))
    

# Как создать 3 функции с одинковым именем, если они затирают друг друга? Загадка от Жака Фреско
def BozoSort(a, b=None, c=None, reverse=False):
    res=[]

    if type(a) == list:
        if (type(a[0]) == list):
            for e in a:
                res+=e
        else:
            res = a
    elif (a is not None and b is not None and c is not None):
        res = [a, b, c]
    else:
        return None

    #Сортировка
    while is_sorted(res,reverse) != True:
        f = randint(0, len(res) - 1)
        l = randint(0, len(res) - 1)
        while l == f:
            f = randint(0, len(res) - 1)
            t = res[f]
            res[f] = res[l]
            res[l] = t
    return res
    
def printResult(a):
    for i in range(len(a)):
        print(a[i],end=' ')
    print('')

n = int(input())
istr = input()
arr = [int(num) for num in istr.split(' ')]
dArr = []
for i in range(int(m.sqrt(len(arr)))):
    dArr.append([])
    for j in range (int(m.sqrt(n))):
        dArr[i].append(arr[int(i*m.sqrt(n)+j)])

printResult(BozoSort(arr, reverse=False))
printResult(BozoSort(arr, reverse=True))
printResult(BozoSort(dArr, reverse=False))
printResult(BozoSort(dArr, reverse=True))
printResult(BozoSort(arr[0], arr[1], arr[2], reverse=False))
printResult(BozoSort(arr[0], arr[1], arr[2], reverse=True))