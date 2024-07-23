"""Advent of code 2023 day1: Trebuchet"""

import argparse
from typing import Iterable

parser = argparse.ArgumentParser(description="Advent of code, day 1 'Trebuchet' solver")
parser.add_argument("file", help="File containing calibration values")
parser.add_argument('-v', help='Print verbose output')

def get_digits(line: str) -> Iterable[str]:
    """Return a list of all digits in a line"""

    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)

    return digits

def main():
    """Entry point"""

    answer = 0
    args = parser.parse_args()
    verbose = args.v

    fname = args.file

    with open(fname, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()
            digits = get_digits(line)
            a, b = (digits[0], digits[-1])
            ab = int(a+b)
            answer += ab
            if verbose:
                print(f"{line}  ->  ({a}, {b}) -> {ab}")

        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
