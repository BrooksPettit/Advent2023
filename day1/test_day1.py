"""Tests for Day1 problem"""

import day1

PART1_SAMPLE = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

PART2_SAMPLE = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

def test_day1_sample():
    """Problem statement sample"""

    ans = day1.part1_sum(PART1_SAMPLE.splitlines())
    assert ans == 142

def test_day1_problem():
    """Main problem statement - part 1"""
    fname = "day1_input.txt"
    with open(fname, 'r', encoding='utf-8') as file:
        ans = day1.part1_sum(file.readlines())
    assert ans == 55477

def test_day2_sample():
    """Part2 with string parsing"""

    ans = day1.part2_sum(PART2_SAMPLE.splitlines())
    assert ans == 281

def test_part2_problem():
    """Part2 from file"""

    with open("day1_input.txt", 'r', encoding='utf-8') as file:
        ans = day1.part2_sum(file.readlines())
    assert ans == 54431
