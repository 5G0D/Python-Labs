import random

gameFlag = True

while gameFlag:
    #Игра
    loseFlag = True
    tryNum = 0

    num = random.randint(0,100)

    print('{Приветственное сообщение от игры}')
    while tryNum < 5:
        tryNum += 1
        playerNum = int(input())
        #Проверка числа
        if playerNum < num:
            print('Загаданное число больше')
        elif playerNum > num:
            print('Загаданное число меньше')
        else:
            print('Поздравляю! Вы угадали')
            loseFlag = False
            break

    if loseFlag:
        print(('Вы проиграли. Было загадано: {n}').format(n=num))

    #Новая игра?
    print('\nХотите начать сначала? (1 - ДА )')
    if int(input()) == 1:
        gameFlag = True
    else:
        gameFlag = False