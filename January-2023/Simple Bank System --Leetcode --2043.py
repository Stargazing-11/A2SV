class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def checkaccount(self, acc1):
        if acc1 < 1:
            return False
        if acc1 > len(self.balance):
            return False
        return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.checkaccount(account1) == False or self.checkaccount(account2) == False:
            return False
        if self.balance[account1 - 1] - money < 0:
            return False
        else:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        if self.checkaccount(account) == False:
            return False
        else:
            self.balance[account - 1] += money
            return True

    def withdraw(self, account: int, money: int) -> bool:
        if self.checkaccount(account) == False:
            return False
        elif self.balance[account - 1] - money < 0:
            return False
        else:
            self.balance[account - 1] -= money
            return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
