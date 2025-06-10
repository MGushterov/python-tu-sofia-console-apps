def problem_1(list):
    max_el = list[0]
    for el in list:
        if max_el < el:
            max_el = el

    return max_el

from collections import deque


my_deque = deque()
my_deque.appendleft()