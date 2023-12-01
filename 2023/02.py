from utils import advent

advent.setup(2023, 1)


def func1(data):
    pass


def func2(data):
    pass


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.readlines()

    advent.print_answer(1, func1(lines))
    # advent.print_answer(2, func2(lines))
    # advent.submit_answer(1, func1(lines))
    # advent.submit_answer(2, func2(lines))
