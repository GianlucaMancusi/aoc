from collections import defaultdict
from utils import advent
import regex as re

advent.setup(2023, 4)


def parse(line):
    line = line.strip()
    card = line.split(':')[0]
    numbers = line.split(':')[1]
    winning = numbers.split('|')[0]
    having = numbers.split('|')[1]
    winning_list = re.findall(r'\d+', winning)
    having_list = re.findall(r'\d+', having)
    return card.split(' ')[-1], winning_list, having_list


def func1(data):
    score = 0
    for line in data:
        _, winning, having = parse(line)
        s = sum(h in winning for h in having)
        score += 2**(s - 1) if s > 0 else 0
    return score


def func2(data):
    scores = defaultdict(int)
    for line in data:
        card, winning, having = parse(line)
        scores[int(card)] += sum(h in winning for h in having)

    copies = {k: 1 for k in scores}
    for s, value in scores.items():
        for i in range(1, value + 1):
            if s + i in copies:
                copies[s + i] += copies[s]

    return sum(copies.values())


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.readlines()

    advent.print_answer(1, func1(lines))
    advent.print_answer(2, func2(lines))
