from Account import Account


class SavingsAccount(Account):
    def __init__(self, account_number, balance, pin, interest_rate):
        super().__init__(account_number, balance, pin)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def calculate_balance_with_interest(self):
        return self.balance + self.calculate_interest()

    def get_savings_account_info(self):
        print(f"Номер на сметката: {self.account_number}")
        print(f"Баланс: {self.calculate_balance_with_interest()}")