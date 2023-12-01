from utils import advent
import re

advent.setup(2023, 1)


def func1(data):
    c = 0
    for d in data:
        num = ''.join([x for x in d if x.isdigit()])
        c += int(num[0] + num[-1])
    return c


def func2(data):
    mapping = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for j, d in enumerate(data):
        indexes = [(i, i + len(word)) for i in range(len(d)) for word in mapping if d.startswith(word, i)]
        new_d = ''
        prev_end = 0
        for start, end in indexes:
            new_d += d[prev_end:start] + mapping[d[start:end]]
            prev_end = end
        new_d += d[prev_end:]
        data[j] = new_d
        
    return func1(data)

if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.readlines()

    advent.print_answer(1, func1(lines))
    advent.print_answer(2, func2(lines))
    # advent.submit_answer(1, func1(lines))
    advent.submit_answer(2, func2(lines))
