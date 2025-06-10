def problem_1(nums_list):
    max_num = nums_list[0]
    for num in nums_list:
        if num > max_num:
            max_num = num
    return max_num

def problem_2(strings):
    for item in strings:
        if len(item) <= 5:
            strings.pop(item)

    return strings

def problem_3(list_1, list_2):
    set_1, set_2 = set(list_1), set(list_2)
    return set_1 & set_2

def problem_4(nums):
    even_nums, odd_nums = [], []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)

    return even_nums, odd_nums

def problem_5(items):
    if len(items) == 0:
        return []

    result = []
    without_first = items[1:]
    result.append([items[0]] + problem_5(without_first))
    return result


print(problem_5(["Man City", "Arsenal", "Chealshit"]))

def problem_6(nums):
    average = sum(nums) / len(nums)
    return list(filter(lambda x: x > average, nums))


def problem_7(nums, value):
    average = sum(nums) / len(nums)
    return [x for x in nums if x < average and x > value]


def problem_9(dictionary):
    filtered = {}
    for name, age in dictionary.items():
        if age > 25:
            filtered[name] = age

    return filtered

def problem_10():
    pass

