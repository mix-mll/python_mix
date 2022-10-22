from math import prod
import numpy as np
from itertools import product  # cartesian product

class GetPins:

    ADJACENTS = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9' , '0'],
        '9': ['9', '6', '8'],
    }

    def get_pins01(observed):
        variations = [GetPins.ADJACENTS[i] for i in observed]
        max_convinations = prod([len(v) for v in variations])
        result = np.array([[''] * len(variations)] * max_convinations)

        mult = 1
        for col in range(len(observed)):
            digits = variations[col]
            row = 0
            for _ in range(max_convinations // mult // len(digits)):
                for digit in digits:
                    result[row: row + mult, col] = digit
                    row += mult
            mult *= len(digits)
        return set(["".join(r) for r in result])

    def get_pins02(observed):
        variations = [GetPins.ADJACENTS[i] for i in observed]
        max_convinations = prod([len(v) for v in variations])
        result = [''] * max_convinations

        mult = 1
        for col in range(len(observed)):
            digits = variations[col]
            row = 0
            for _ in range(max_convinations // mult // len(digits)):
                for digit in digits:
                    for j in range(mult):
                        result[row + j] += digit
                    row += mult
            mult *= len(digits)
        return set(result)

    def get_pins03(observed):
        GetPins.ADJACENTS
        if len(observed) == 1:
            return set(GetPins.ADJACENTS[observed])
        return set([a + b for a in  GetPins.ADJACENTS[observed[0]] for b in GetPins.get_pins03(observed[1:])])

    def get_pins04(observed):
        # steps
        # variations = [GetPins.ADJACENTS[i] for i in observed]
        # all_pins_array = product(*variations)
        # all_pins_str = ["".join(pin) for pin in all_pins_array]
        # return set(all_pins_str)

        # two lines
        #variations = [GetPins.ADJACENTS[i] for i in observed]
        #return set(["".join(pin) for pin in product(*variations)])

        # one line
        return set(["".join(pin) for pin in product(*(GetPins.ADJACENTS[i] for i in observed))])

    def get_pins05(observed):
        ADJACENTS2 = ["".join(values) for values in GetPins.ADJACENTS.values()]
        return set(["".join(pin) for pin in product(*(ADJACENTS2[int(i)] for i in observed))])



    def test_get_pins():

        fun_list = [
            GetPins.get_pins01,
            GetPins.get_pins02,
            GetPins.get_pins03,
            GetPins.get_pins04,
            GetPins.get_pins05,
        ]

        test_cases = [
            ('0', ['0', '8']),
            ('1', ['1', '2', '4']),
            ('01', ['01', '02', '04','81', '82', '84']),
            ('8', ['5','7','8','9','0']),
            ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
            ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])
        ]

        def _assert_(fun, input, expected):
            result = fun(input)
            if not result == expected:
                print(f"{fun=} {input=} {result=} {expected=}")
            assert result == expected
        
        for fun in fun_list:
            print(fun)
            [_assert_(fun, input, set(expected)) for input, expected in test_cases]
            
        print("GetPins tested")
    

GetPins.test_get_pins()