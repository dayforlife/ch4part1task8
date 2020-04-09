class MoneyFmt():
    def __init__(self, money):
        self.money = money

    def update(self, new_money):
        self.money = new_money
        

    def __repr__(self):
        result = str(self.money)
        print(result)
        return result
        

    def __str__(self):
        self.result = ('${:,.2f}'.format(self.money))
        return self.result
