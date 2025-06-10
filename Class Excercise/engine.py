from Account import Account
from SavingsAccount import SavingsAccount
from Bank import Bank


bank = Bank()


def initialize_bank_accounts():
    while True:
        try:
            accounts_amount = int(input("Въведете колко на брой банкови сметки искате да отворите: "))
        except ValueError as val_er:
            print(val_er, "Въведете брой банкови сметки в числов вид!")
        else:
            counter = 0
            bank_account = None
            while counter != accounts_amount:
                try:
                    account_number = input("Номер на сметката: ")
                    initital_balance = float(input("Начален баланс: "))
                    pin = input("ПИН код: ")
                    while True:
                        type_of_account = input("Вид на сметката: ")

                        if type_of_account == "Спестовна":
                            interest_rate = float(input("Лихвен процент: "))
                            bank_account = SavingsAccount(account_number, initital_balance, pin, interest_rate)
                            break
                        elif type_of_account == "Разплащателна":
                            bank_account = Account(account_number, initital_balance, pin)
                            break
                        else:
                            print("Въведете правилен вид на сметката!")

                except Exception as msg:
                    print(msg)
                else:
                    bank.add_account(bank_account)
                    counter += 1

            return


def initialize_bank_menu():
    print("""------------------
------------------
Меню
------------------
------------------""")
    counter = 1

    for account in bank.bank_accounts:
        print(f"""{counter}. {account.get_account_number()}: 
        {account.get_balance()}
        {account.get_pin()}
----------------
----------------""")
        counter += 1


def initialize_bank_account_menu():
    print("""------------------
------------------
МЕНЮ
------------------
------------------
1. Депозит
2. Теглене
3. Инфо за сметката
4. Върнете се в главното меню
------------------
------------------""")


def initialize_bank_details():
    while True:
        initialize_bank_menu()
        account_number = input("Въведете номера на сметката, която желаете да достъпите: ")
        flag = False
        account = None
        for acc in bank.bank_accounts:
            if account_number == acc.get_account_number():
                account = acc
                flag = True

        if not flag:
            print("Въведете номера на съществуваща сметка")
            continue
        else:
            break

    index = bank.bank_accounts.index(account)
    initialize_bank_account_details(bank.bank_accounts[index])


def initialize_bank_account_details(bank_account):
    while True:
        initialize_bank_account_menu()
        try:
            operation = int(input("Въведете номер на операция: "))
        except ValueError as val_er:
            print(val_er, "Въведете операция в числов вид!")
        else:
            if operation == 1:
                deposit = float(input("Депозит: "))
                bank_account.deposit(deposit)
            elif operation == 2:
                amount_to_withdraw = float(input("Сума за теглене: "))
                pin = input("ПИН код: ")
                try:
                    bank_account.withdraw(amount_to_withdraw, pin)
                except Exception as err:
                    print(err)
            elif operation == 3:
                if type(bank_account) == Account:
                    bank_account.stringify_account_details()
                elif type(bank_account) == SavingsAccount:
                    bank_account.get_savings_account_info()
                break
            elif operation == 4:
                initialize_bank_details()
                break
            else:
                print("Въведете число между 1 и 4!")

