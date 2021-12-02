import math


class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x = math.pow(self.coor1[0] - self.coor2[0], 2)
        y = math.pow(self.coor1[1] - self.coor2[1], 2)
        return math.sqrt(x+y)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


class TestLine:
    coordinate1 = (2, 3)
    coordinate2 = (8, 10)

    l = Line(coordinate1, coordinate2)

    print(l.distance())
    print(l.slope())


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * (math.pow(self.radius, 2)) * self.height

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * math.pow(self.radius, 2))


class TestCylinder:
    c = Cylinder(2, 3)

    print(c.volume())
    print(c.surface_area())


#Object Oriented Programming

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        print("Deposit of ${} has been accepted.".format(amount))
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Withdraw of ${} not accepted. Funds Unavailable!".format(amount))
        else:
            print("Withdrawal of ${} accepted.".format(amount))
            self.balance = self.balance - amount

    def __str__(self):
        return "Owner: {} \nBalance: {}".format(self.owner, self.balance)


class TestAccount:
    jeff_acc = Account("Jeff", 300)
    print(jeff_acc)

    jeff_acc.deposit(200)
    print(jeff_acc)

    jeff_acc.withdraw(600)
    print(jeff_acc)

    jeff_acc.withdraw(500)
    print(jeff_acc)
