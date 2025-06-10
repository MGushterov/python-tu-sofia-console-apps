size = int(input("Enter list size: "))

numbers = []
for i in range(size):
    num = int(input("Enter a number: "))
    numbers.append((num))

average = sum(numbers) / len(numbers)
print(numbers)
print(average)