"""Advent of code 2023 day1: Trebuchet"""

from typing import Dict, List

TOKEN_MAP = {
         "one": 1,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven": 7,
         "eight": 8,
         "nine": 9,
         }

reversed_token_map = {}
for key,value in TOKEN_MAP.items():
    reversed_token_map[key[::-1]] = value

def part2_get(line: str, tok_map: Dict[str, int]) -> str:
    """Return first digit or number string in line"""

    while line:
        c = line[0]
        if c.isdigit():
            return c
        for key,value in tok_map.items():
            if line[:len(key)] == key:
                return str(value)
        line = line[1:]

    raise ValueError(f"No digit or digit string in line {line}!")

def part2_get_last(line: str) -> str:
    """Return alst digit or digit string in line"""

    line = line[::-1]
    return part2_get(line, reversed_token_map)

def part2_sum(lines: List[str]) -> int:
    """Process all lines and get sum for aprt2 2 rules"""

    answer = 0
    for l in lines:
        l = l.strip()
        if not l:
            continue
        a = part2_get(l, TOKEN_MAP)
        b = part2_get_last(l)
        ab = a+b
        print(ab)
        answer += int(ab)
    return answer

def get_digits(line: str) -> List[str]:
    """Return a list of all digits in a line"""

    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)

    return digits

def part1_sum(lines) -> int:
    """Get calibration file sum of digits"""
    answer=0
    for l in lines:
        if l.strip() == "":
            continue
        digits = get_digits(l)
        if len(digits) == 1:
            a,b = (digits[0], digits[0])
        else:
            a,b = (digits[0], digits[-1])
        ab = int(a+b)
        answer += ab

    return answer

def main():
    """Entry point"""

    fname = "day1_input.txt"
    with open(fname, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ans1 = part1_sum(lines)
        ans2 = part2_sum(lines)

    print(f"Part1 answer: {ans1}")
    print(f"Part2 answer: {ans2}")



if __name__ == "__main__":
    main()
