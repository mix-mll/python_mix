"""
    pytest ews/ews_interview_test.py --log-cli-level=INFO
"""

import logging


def funX(input):
    result = ""
    index = 0
    count = 1
    while index < len(input):
        letter = input[index]
        if index == len(input) - 1:
            result += f"{letter}{count}"
            break
        if letter == input[index + 1]:
            count += 1
        else:
            result += f"{letter}{count}"
            letter = input[index + 1]
            count = 1
        index += 1
    return result


def funX0(input):
    result = ""
    index = 0
    count = 1
    while index < len(input):
        letter = input[index]
        if index + 1 < len(input):
            if letter == input[index + 1]:
                count += 1
            else:
                result += f"{letter}{count}"
                letter = input[index + 1]
                count = 1
        else:
            result += f"{letter}{count}"
        index += 1
    return result


def fun(input):
    result = ""
    letter = input[0]
    count = 1
    for i in range(1, len(input)):
        if letter == input[i]:
            count += 1
        else:
            result += f"{letter}{count}"
            letter = input[i]
            count = 1
    else:
        result += f"{letter}{count}"

    return result


def test_fun():
    cases = {
        "aabbba": "a2b3a1",
        "ab": "a1b1",
        "abc": "a1b1c1",
        "a": "a1",
        "aa": "a2",
        "abccc": "a1b1c3",
    }
    for input, expected_output in cases.items():
        actual_output = fun(input)
        logging.info(f"{input} {expected_output} {actual_output}")
        assert expected_output == actual_output
