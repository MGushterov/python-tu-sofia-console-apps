size = int(input("Enter list size: "))

numbers = []
for i in range(size):
    num = int(input("Enter a number: "))
    numbers.append((num))

sorted_nums = sorted(numbers)
biggest_num, smallest_num = sorted_nums[-1], sorted_nums[0]
print(biggest_num)
print(smallest_num)