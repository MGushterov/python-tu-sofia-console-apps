class Bank:
    def __init__(self):
        self.bank_accounts = []

    def add_account(self, account):
        self.bank_accounts.append(account)
        print("Успешно добавяне на банкова сметка")
