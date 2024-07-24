"""Tests for Day1 problem"""

import day1

SAMPLE_LINES = """
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

    ans = day1.get_sum(SAMPLE_LINES.splitlines())
    assert ans == 281
