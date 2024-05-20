class Worker:

    def __init__(self, name: str, pay: float):
        self.name = name
        self.pay = pay

    def __repr__(self):
        return self.name + ': ' + str(self.pay)

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent=0.05):
        print('Подняли зарплату:', self, f'на {percent * 100}%')
        self.pay *= (1.0 + percent)
        return self

    def fullName(me):
        return me.name


print('Worker.class')

bob = Worker('Bob Smith', 50347.5)
print(bob.lastName())
sue = Worker('Sue Jones', 70647.5)

print(bob)
print(sue)

bob.giveRaise().giveRaise().giveRaise()
sue.giveRaise()

print(bob)
print(sue)
print(sue.fullName())
print(Worker.fullName(sue))
