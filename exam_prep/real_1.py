nums_list = []

while True:
    n = int(input('Enter a number greater than 15 and smaller than 35: '))
    if n > 15 and n < 35:
        i = 0
        while i < n:
            num = int(input('enter a number between 30 and 300: '))
            if num > 30 and num < 300:
                nums_list.append(num)
                i += 1
            else:
                print('Please enter a valid number')
                continue
        break
    else:
        print('Please enter a valid number')
        continue

print(nums_list)

count = 0
searched_index = -1
min_el = 0
for i in range(len(nums_list)):
    desetica = (nums_list[i] // 10) % 10
    print(desetica)
    if desetica % 3 == 0:
        count += 1

    if nums_list[i] // 6 == 4 and (nums_list[i] < min_el or min_el == 0):
        searched_index = i
        min_el = nums_list[i]

print(count)
print(searched_index)

second_nums_list = [x for x in nums_list if x % 2 == 0 or x % 3 == 0]
print(second_nums_list)

sum = 0
odd_indices_count = 0
min_even_num = 0
for i in range(len(second_nums_list)):
    if i % 2 != 0:
        sum += second_nums_list[i]
        odd_indices_count += 1

    if second_nums_list[i] % 2 == 0 and (second_nums_list[i] < min_even_num or min_even_num == 0):
        min_even_num = second_nums_list[i]

average = sum / odd_indices_count

print(average)
print(min_even_num)