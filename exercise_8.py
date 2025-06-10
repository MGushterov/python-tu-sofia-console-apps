size = int(input("Enter list size: "))

numbers = []
for i in range(size):
    num = int(input("Enter a number: "))
    numbers.append((num))

power_list = list(map(lambda num: num ** 2, numbers))
print(numbers)
print(power_list)
