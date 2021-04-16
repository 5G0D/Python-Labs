
print("Введите количество банкнот")
n = int(input())
print("Введите банкноты")
bStr = input()
b = ''

for a in bStr.split(' '):
    if a[0] == 'a' and a[4] == '5' and a[5] == '5' and a[6] == '6' and a[7] == '6' and a[8] == '1':
        b += '\n' + a
    
if b == '':
    print(-1)
else:
    print('Ответ:' + b)

