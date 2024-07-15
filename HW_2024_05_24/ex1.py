class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100
    
    @dollars.setter
    def dollars(self, value):
        if not isinstance(value, int) or value < 0:
            print('dollars error')
        else:
            self.total_cents = self.total_cents - self.dollars * 100 + value * 100

    @property
    def cents(self):
        return self.total_cents % 100
    
    @cents.setter
    def cents(self, value):
        if not isinstance(value, int) or value < 0 or value > 99:
            print('cents error')
        else:
            self.total_cents = self.total_cents - self.cents + value
    
    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
    

Bill = Money(101, 99)
print(Bill)
print(Bill.dollars, Bill.cents)
print(Bill.total_cents)
Bill.dollars = 666
print(Bill)
Bill.cents = 12
print(Bill)