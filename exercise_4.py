size = int(input("Enter list size: "))

numbers = []
for i in range(size):
    num = int(input("Enter a number: "))
    numbers.append((num))

sorted_nums = []
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[i]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
