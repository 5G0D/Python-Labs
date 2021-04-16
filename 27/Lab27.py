
def printMin(a):
    a.sort()
    res = []
    for i in range(5):
        if len(a)>i:
            res.append(a[i])
        else:
            break
    res.sort(reverse=True)
    for i in range(len(res)):
        print(res[i],end=' ')
    print()

print('Введите кол-во сигналов')
n = int(input())
arr = []
print('Введите сигналы через ENTER')
for i in range(n):
    arr.append(int(input()))
    printMin(arr)