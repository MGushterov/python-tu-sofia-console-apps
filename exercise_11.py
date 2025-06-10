def calculate_tax_rate(income):
    tax_rate = 0.0
    if income <= 10000:
        tax_rate = 0.1
    elif income <= 20000:
        tax_rate = 0.15
    elif income <= 30000:
        tax_rate = 0.2
    else:
        tax_rate = 0.25

    return tax_rate

def print_tax_information(income, tax_rate):
    income_tax = income * tax_rate
    print(f"Income: {income}, Income tax: {income_tax}")

income = float(input("enter your income: "))
print_tax_information(income, calculate_tax_rate(income))