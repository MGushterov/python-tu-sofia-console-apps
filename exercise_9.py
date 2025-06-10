import string
import sys
import random

def problem_1():
    numbers = input("enter 10 positive numbers: ").split()
    numbers = list(map(lambda num: int(num), numbers))

    numbers = numbers[::2]

    max_num, min_num = int(-sys.maxsize), int(sys.maxsize)
    for num in numbers:
        if num > max_num:
            max_num = num

        if num < min_num:
            min_num = num

    print(f"biggest num is: {max_num}")
    print(f"smallest num is: {min_num}")

    sorted_ascending = sorted(numbers)
    sorted_descending = sorted(numbers, reverse=True)

    print(sorted_ascending)
    print(sorted_descending)

def problem_2(): #list 15 nums random from 1 to 100 and add num inbetween each two elements
    random_nums_list = []
    for i in range(15):
        random_nums_list.append(random.randint(1, 101))

    print(random_nums_list)
    #random_nums_list_with_sums = random_nums_list.copy()
    for j in range(0, len(random_nums_list)):
        #sum_of_two = random_nums_list[j] + random_nums_list[j-1]
        #random_nums_list_with_sums.insert(j + j - 1, sum_of_two)
        if j % 2 != 0:
            random_nums_list.insert(j, random_nums_list[j] + random_nums_list[j - 1])

    print(random_nums_list)


def problem_3():
    list_of_letters_one, list_of_letters_two = [], []

    for i in range(10):
        list_of_letters_one.append(random.choice(string.ascii_lowercase))
        list_of_letters_two.append(random.choice(string.ascii_lowercase))

        all_elements_list = list_of_letters_one + list_of_letters_two
        uncommon_in_second_list = []

        for el in list_of_letters_two:
            if el not in list_of_letters_one:
                uncommon_in_second_list.append(el)

        #2 lists with 10 letters (lower case), two lists, first - all elements, second - with those that can be found in one but not the other (using 2nd list

#problem_1()
#problem_2()
problem_3()

