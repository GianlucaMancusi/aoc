from collections import defaultdict
import itertools
from utils import advent
import numpy as np


advent.setup(2023, 3)


def parse_matrix(lines):
    m = [list(line.strip()) for line in lines]
    return np.array(m)


def check_adjacent(matrix, i, j):
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    height, width = kernel.shape
    h, w = matrix.shape
    for k, l in itertools.product(range(height), range(width)):
        if kernel[k, l] == 1:
            if 0 <= i + k - 1 < h and 0 <= j + l - 1 < w:
                if matrix[i + k - 1, j + l - 1] not in ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    return True
    return False


def check_gear(matrix, i, j):
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    height, width = kernel.shape
    h, w = matrix.shape
    for k, l in itertools.product(range(height), range(width)):
        if kernel[k, l] == 1:
            if 0 <= i + k - 1 < h and 0 <= j + l - 1 < w:
                if matrix[i + k - 1, j + l - 1] in ('*',):
                    return (i + k - 1, j + l - 1)
    return False


def func1(data): 
    matrix = parse_matrix(data)
    height, width = matrix.shape

    n_adj_to_symb = []

    number = []
    is_symb = False
    for i in range(width):
        for j in range(height):
            if matrix[i, j].isdigit():
                number.append(matrix[i, j])
                if check_adjacent(matrix, i, j):
                    is_symb = True
            else:
                if is_symb:
                    n_adj_to_symb.append(int(''.join(number)))
                number = []
                is_symb = False
    return sum(n_adj_to_symb)


def func2(data):
    matrix = parse_matrix(data)
    height, width = matrix.shape

    n_adj_to_symb = []

    number = []
    is_symb = False
    gears = defaultdict(list)
    current_gears = set()
    for i in range(width):
        for j in range(height):
            if matrix[i, j].isdigit():
                number.append(matrix[i, j])
                if check_adjacent(matrix, i, j):
                    is_symb = True
                gear = check_gear(matrix, i, j)
                if gear != False:
                    current_gears.add(gear)
            else:
                if is_symb:
                    n_adj_to_symb.append(int(''.join(number)))
                    for gear in current_gears:
                        gears[gear].append(int(''.join(number)))
                number = []
                is_symb = False
                current_gears = set()

    valid_gears = []
    for gear, numbers in gears.items():
        if len(numbers) == 2:
            valid_gears.append(np.prod(numbers))

    return sum(valid_gears)


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.readlines()

    advent.print_answer(1, func1(lines))
    advent.print_answer(2, func2(lines))
