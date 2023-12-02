from utils import advent
from collections import defaultdict

advent.setup(2023, 2)


def parse_game(line):
    sub_sets = defaultdict(int)
    game, bags = line.split(':')
    for bag in bags.split(';'):
        for box in bag.split(','):
            _, number, color = box.split(' ')
            sub_sets[color] = max(sub_sets[color], int(number))
    return game.split(' ')[1], sub_sets


def loop(data, requested_function):
    output = 0
    for line in data:
        game_id, s = parse_game(line.strip())
        output += requested_function(game_id, s['red'], s['green'], s['blue'])
    return output


def func1(data):
    return loop(data, lambda g_id, r, g, b: int(g_id) if r <= 12 and g <= 13 and b <= 14 else 0)


def func2(data):
    return loop(data, lambda g_id, r, g, b: r * g * b)


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.readlines()

    advent.print_answer(1, func1(lines))
    advent.print_answer(2, func2(lines))
