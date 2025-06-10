class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = self.set_account_number(account_number)
        self.balance = self.set_balance(balance)
        self.pin = self.set_pin(pin)

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, value):
        val_arr = value.split()
        if len(val_arr) != 4:
            raise Exception("Невалиден номер на банкова сметка! Опитайте отново")

        return value

    def get_balance(self):
        return self.balance

    def set_balance(self, value):
        if value < 0:
            raise Exception("Балансът не може да бъде по-малък от нула")

        return value

    def get_pin(self):
        return self.pin

    def set_pin(self, value):
        if len(value) != 4:
            raise Exception("ПИН кодът трябва да бъде точно 4 цифри")

        for char in value:
            if ord(char) < 48 or ord(char) > 57:
                raise Exception("ПИН кодът трябва да съдържа само числа")

        return value

    def deposit(self, amount):
        self.balance += amount

    def validate_amount_to_withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise Exception("Нема паре!")

    def withdraw(self, amount, pin):
        if pin == self.pin:
            self.validate_amount_to_withdraw(amount)
        else:
            raise Exception("Въведете правилния ПИН!")

    def stringify_account_details(self):
        print(f"Номер на сметката: {self.account_number}")
        print(f"Баланс: {self.balance}")