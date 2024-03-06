from collections import Counter
from itertools import permutations
from math import factorial, prod


class AlphabeticAnagrams:
    """
    We can then assign a number to every word,
    based on where it falls in an alphabetically sorted
    list of all words made up of the same group of letters.
    One way to do this would be to generate the entire list of words and find the desired one,
    but this would be slow if the word is long.
    """

    def get_distinct_permutations_slow(sub_letter, count):
        letters = []
        for let, n in count.items():
            if let == sub_letter:
                n -= 1
            for i in range(n):
                letters.append(let)
        unique_permutations = set()
        for i in permutations(letters):
            unique_permutations.add(i)
        return len(unique_permutations)

    def get_distinct_permutations_01(sub_letter, count):
        i = 0
        divisor = 1
        for letter, c in count.items():
            if letter == sub_letter:
                c -= 1
            # divisor = divisor * factorial(c)
            divisor *= factorial(c)
            i += c
        return factorial(i) // divisor

    def get_distinct_permutations_02(sub_letter, count):
        factors = {
            2: {2: 1},
            3: {3: 1},
            4: {2: 2},
            5: {5: 1},
            6: {2: 1, 3: 1},
            7: {7: 1},
            8: {2: 3},
            9: {3: 2},
            10: {2: 1, 5: 1},
            11: {11: 1},
            12: {2: 2, 3: 1},
            13: {13: 1},
            14: {2: 1, 7: 1},
            15: {3: 1, 5: 1},
            16: {2: 4},
            17: {17: 1},
            18: {2: 1, 3: 2},
            19: {19: 1},
            20: {2: 2, 5: 1},
            21: {3: 1, 7: 1},
            22: {2: 1, 11: 1},
            23: {23: 1},
            24: {2: 3, 3: 1},
            25: {5: 2},
            26: {2: 1, 13: 1},
        }

        i = 0
        divisors = Counter({})
        for letter, c in count.items():
            if letter == sub_letter:
                c -= 1
            for j in range(2, c + 1):
                divisors += factors.get(j, {j: 1})
            i += c

        divident = Counter({})
        for k in range(2, i + 1):
            divident += factors.get(k, {k: 1})
        result_factors = divident - divisors
        # print("results:")
        result = prod([k**n for k, n in result_factors.items()])
        # print(result_factors, result)
        return result

    def get_positions(word, subfuntion=get_distinct_permutations_02):
        result = 1
        count = Counter(word)
        for i in range(len(word)):
            letter = word[i]
            for sub_letter in count:
                # if ord(sub_letter) >= ord(letter): # only letter that are first alph
                if sub_letter >= letter:
                    continue
                result += subfuntion(sub_letter, count)
            count[letter] -= 1
            if count[letter] == 0:
                count.pop(letter)
        return result

    def get_positions_01(word, *k):
        len_word = len(word)
        s = 1
        result = 1
        count = Counter()
        for i in range(len_word):
            letter = word[len_word - 1 - i]
            count[letter] += 1
            for sub_letter in count:
                if not sub_letter < letter:
                    continue
                result += s * count[sub_letter] // count[letter]
            s = s * (i + 1) // count[letter]
        return result

    def get_positions_02(word, *k):
        def calc_word_perm(word):
            divisor = 1
            for count in Counter(word).values():
                divisor *= factorial(count)
            return factorial(len(word)) // divisor

        if len(word) > 1:
            result = (sorted(word).index(word[0]) * calc_word_perm(word)) // len(word)
            result += AlphabeticAnagrams.get_positions_02(word[1:])
        else:
            result = 1

        return result

    def testAlphabeticAnagrams():
        test_values = {
            "A": 1,
            "B": 1,
            "AB": 1,
            "BA": 2,
            "AAB": 1,
            "ABA": 2,
            "BAA": 3,
            "AAAB": 1,
            "ABAB": 2,
            "BAAA": 4,
            "QUESTION": 24572,
            "BOOKKEEPER": 10743,
        }
        sub_fun_list = [
            (
                AlphabeticAnagrams.get_positions,
                [
                    AlphabeticAnagrams.get_distinct_permutations_slow,
                    AlphabeticAnagrams.get_distinct_permutations_01,
                    AlphabeticAnagrams.get_distinct_permutations_02,
                ],
            ),
            (AlphabeticAnagrams.get_positions_01, [None]),
            (AlphabeticAnagrams.get_positions_02, [None]),
        ]

        for fun, sub_functions in sub_fun_list:
            for sub_sub in sub_functions:
                for word, expected in test_values.items():
                    result = fun(word, sub_sub)
                if expected != result:
                    print(f"{word=} {result=} {expected=} ")
                assert expected == result

        print("AlphabeticAnagrams test")


AlphabeticAnagrams.testAlphabeticAnagrams()
