from aoc_2021.utils import get_input, pretty_print_solutions


def preprocess(input_data):
    splitted = input_data.splitlines()
    rules = {}
    for line in splitted[2:]:
        input_letters, output_letter = map(str, line.split(' -> '))
        rules[input_letters] = (
            input_letters[0] + output_letter,
            output_letter + input_letters[1]
        )
    return rules, {k: splitted[0].count(k) for k in rules}


def run_iteration(rules, counter):
    new_counter = {k: 0 for k in counter}
    for rule in rules:
        if counter[rule] != 0:
            for next_rule in rules[rule]:
                new_counter[next_rule] += counter[rule]
    return new_counter


def count_occurences(counter):
    letters_counter = {k: 0 for k in list(set([x[0] for x in counter] + [x[1] for x in counter]))}
    for rule in counter:
        letters_counter[rule[1]] += counter[rule]
    return letters_counter


def compute_flag(letters_counter):
    return max(list(letters_counter.values())) - min(list(letters_counter.values()))


if __name__ == '__main__':
    input_data = get_input('https://adventofcode.com/2021/day/14/input')
    rules, counter = preprocess(input_data)

    for i in range(40):
        if i == 10:
            solution_first_part = compute_flag(count_occurences(counter))
        counter = run_iteration(rules, counter)

    solution_second_part = compute_flag(count_occurences(counter))

    pretty_print_solutions(solution_first_part, solution_second_part, 14)
