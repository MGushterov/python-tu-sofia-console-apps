nums_list_1, nums_list_2 = [], []
user_input = int(input("Enter a number: "))

while user_input != 0:
    if user_input % 3 == 0 and user_input % 2 == 0:
        nums_list_1.append(user_input)

    if user_input % 7 == 0 and user_input % 2 != 0:
        nums_list_2.append(user_input)

    user_input = int(input("Enter a number: "))

sum_of_list1_odd_indices = sum([nums_list_1[i] for i in range(len(nums_list_1)) if i % 2 != 0])

nums_list_2.sort(reverse=True)
result = nums_list_2[0] * nums_list_2[-1]

print(sum_of_list1_odd_indices)
print(result)
