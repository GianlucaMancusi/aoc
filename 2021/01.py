from utils import advent

advent.setup(2021, 1)


def func1(data):
    return sum([int(data[i]) < int(data[i + 1]) for i in range(len(data) - 1)])


def func2(data):
    nums = [int(i) for i in data]
    nums = [sum(nums[i:i + 3]) for i in range(len(nums) - 2)]
    return func1(nums)


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.readlines()

    advent.print_answer(1, func1(lines))
    advent.print_answer(2, func2(lines))
    # advent.submit_answer(1, func1(lines))
    # advent.submit_answer(2, func2(lines))
