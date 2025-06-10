size = int(input("Enter list size: "))

numbers = []
for i in range(size):
    num = int(input("Enter a number: "))
    numbers.append((num))


sum = 0
for i in range(len(numbers)):
    if i % 2 == 0:
        sum += numbers[i]

print(sum)