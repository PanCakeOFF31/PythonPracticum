class Worker:
    def __init__(self, name: str, pay: float):
        self.name = name
        self.pay = pay

    def __repr__(self):
        return f'Worker.class({self.name} : {self.pay})'

    def __str__(self):
        return self.name + ': ' + str(self.pay)

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent=0.05):
        print('Подняли зарплату:', self, f'на {percent * 100}%')
        self.pay *= (1.0 + percent)
        return self

    def fullName(me):
        return me.name

    def __add__(self, other):
        return self.pay + other.pay


print(type(Worker))

bob = Worker('Bob Smith', 50347.5)
print(bob.lastName())
sue = Worker('Sue Jones', 70647.5)

print(bob)
print(repr(bob))
print(sue)
print(repr(sue))

bob.giveRaise().giveRaise().giveRaise()
sue.giveRaise()

print(bob)
print(sue)
print(sue.fullName())
print(Worker.fullName(sue))

print("Зарпалата bob", bob.pay)
print("Зарпалата sue", sue.pay)
# Реализован перегруженный метод __add__ для суммирования зарплат
print("Сумма зарплат двух сотрудников:", bob + sue)
