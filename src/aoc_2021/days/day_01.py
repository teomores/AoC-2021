from aoc_2021.utils import get_input, pretty_print_solutions


def prepare_input(challenge_input: str) -> list[int]:
    return [int(x) for x in challenge_input.splitlines()]


def solve_first_part(params: list) -> int:
    difference_list = [params[i+1]-params[i] for i in range(len(params)-1)]
    return sum(i > 0 for i in difference_list)


def solve_second_part(params: list) -> int:
    difference = [params[i+3]-params[i] for i in range(len(params)-3)]
    return sum(i > 0 for i in difference)


if __name__ == '__main__':
    # Get and prepare the challenge input.
    challenge_input = get_input('https://adventofcode.com/2021/day/1/input')
    challenge_prepared_input = prepare_input(challenge_input)

    solution_first_part = solve_first_part(challenge_prepared_input)
    solution_second_part = solve_second_part(challenge_prepared_input)

    pretty_print_solutions(solution_first_part, solution_second_part, 1)
