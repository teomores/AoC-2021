import requests
import yaml
from prettytable import PrettyTable


COOKIES_PATH = 'cookies.yml'
DAILY_URL = 'https://adventofcode.com/2021/day/'


def get_input(url: str) -> str:
    with open(COOKIES_PATH) as cookie_file:
        cookies = yaml.load(cookie_file, Loader=yaml.FullLoader)
    return requests.get(url, cookies=cookies).text


def pretty_print_solutions(
    solution_first_part: str,
    solution_second_part: str,
    challenge_number: int
) -> None:
    print(f"These are the solutions to your Day {challenge_number} inputs:\n")
    solution_table = PrettyTable(['', 'Solution'])
    solution_table.add_row(['Part 1', solution_first_part])
    solution_table.add_row(['Part 2', solution_second_part])
    print(solution_table)
    print(f"\nSubmit your solutions here ~> {DAILY_URL}{challenge_number}")
