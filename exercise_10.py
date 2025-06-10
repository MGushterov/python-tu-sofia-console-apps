def problem_1():
    list_names = input("Enter names: ").split(' ')
    list_ages = input("Enter ages: ").split(' ')
    tuples_name_age = zip(list_names, list_ages)
    print(tuple(tuples_name_age))


def problem_2():
    list_nums = input("Enter numbers: ").split(' ')
    parsed_list_nums = [int(x) for x in list_nums]
    list_nums_powered = [int(x)**2 for x in list_nums]
    list_of_tuples = dict(zip(parsed_list_nums, list_nums_powered))
    print(list_of_tuples)


def problem_3():
    list = input("Enter key-value in dict format: ").split(' ')
    dictionary = {}
    for item in list:
        key, value = item.split(':')
        value = int(value)
        if value > 10:
            dictionary[key] = value

    print(dictionary)


def problem_4():
    list_of_nums = input("Enter numbers: ").split(" ")
    set_of_nums = set(list_of_nums)
    dict = {}

    for num in set_of_nums:
        count = list_of_nums.count(num)
        dict[num] = count
    print(dict)
# problem_1()
# problem_2()
problem_3()
# problem_4()