class Drink:
    def __init__(self, str):
        arr = str.split(' ')
        self.name = arr[0]
        self.price = int(arr[1])
        self.v = int(arr[2])

    def calcV(self, m):
        return (m // self.price) * self.v

    def print(self, m):
        print(self.name, m // self.price)
        print(self.calcV(m))
        print(m % self.price)

money = int(input())
count = int(input())

topDrink = None
maxV = 0

for i in range(count):
    drink = Drink(input())
    if maxV < drink.calcV(money):
        maxV = drink.calcV(money)
        topDrink = drink

print('')
if topDrink is None:
    print(-1)
else:
    topDrink.print(money)