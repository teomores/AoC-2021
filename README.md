![AoC](https://blogs.sap.com/wp-content/uploads/2020/11/EkaoQQTXEAMA4BN.jpg)
# AoC-2021
This repo contains my solutions to the [Advent of Code - 2021](https://adventofcode.com/2021) challenges.

## Installation
After cloning this repo, follow these steps to setup the project:
1. Install [Poetry](https://python-poetry.org/).
2. Run `poetry install`.
3. Log in with you AoC credentials and get your cookies to be able to run the solvers on your personal inputs. Once you have your cookies, create a file named `cookies.yml` in the main folder of the project. This file should look like this:
```yml
_ga: GA1.YOUR_NUMBERS
_gid: GA1.YOUR_NUMBERS
session: YOUR_SESSION_ID
```

## Solve
This repo can be used for solving your daily AoC 2021 puzzles. To solve a specific day:
```sh
poetry run poe solve -d YOUR_DAY
```
Days are numbered in two digits, so in order to solve Day 5 you should run `poetry run poe solve -d 05`.
