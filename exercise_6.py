size = int(input("Enter list size: "))

numbers = []
for i in range(size):
    num = int(input("Enter a number: "))
    numbers.append((num))

filtered_nums = list(filter(lambda num: num % 3 == 0, numbers))
print(filtered_nums)