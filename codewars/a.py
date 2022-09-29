class RangeExtraction:
    """
    Range Extraction

    A format for expressing an ordered list of integers is to use a comma separated list of either individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.

    The range includes all integers in the interval including both endpoints.
    It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

    Complete the solution so that it takes a list of integers in increasing order
    and returns a correctly formatted string in the range format.
    solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
    Example:
    """
    def get_range(args):
        list_range = ",".join([str(i) for i in args])
        return list_range


    def get_range(args_raw):
        elements = []
        range_count = 0
        args = sorted(args_raw)
        start_range_k = args[0]
        for i in range(1, len(args)):
            print(f"\t {i=} p={args[i-1]} n={args[i]}")
            if args[i-1] - args[i] == -1:
                print(f"\t\t  increment")
                if range_count == 0:
                    start_range_k = args[i-1]
                range_count += 1

            elif range_count > 1:
                print(f"\t\t  no increment finish range")
                elements.append(f"{start_range_k}-{args[i-1]}")
                range_count = 0
            else:
                k = args[i-range_count-1]
                start_range_k = args[i-1]
                print(f"\t\t no increment single {range_count=} {k=}")

                #elements.append(f"{args[i-1]}")
                elements.append(f"{k}")


        if range_count > 1:
            elements.append(f"{start_range_k}-{args[i]}")
        else:
            elements.append(f"{args[i]}")

        return ",".join(elements)

    def test_range_extraction():
        print("test: RangeExtraction")
        test_data = {
            "1,3,5": [1, 3, 5],
            "1-3,5": [1, 2, 3, 5],
            "1,3-5": [1, 3, 4, 5],
            "1-3": [1, 2, 3],
            '-6,-3-1': [-6,-3,-2,-1,0,1],
            "-3--1,2,10,15,16,18-20": [-3,-2,-1,2,10,15,16,18,19,20],
            #'-6,-3-1,3-5,7-11,14,15,17-20': [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20],
        }
        for expected, input in test_data.items():
            result = RangeExtraction.get_range(input)
            print(f"  result: {result}")
            print(f"expected: {expected}")
            assert  expected == result


def solution(args):
    # your code here
    return RangeExtraction.get_range(args)

RangeExtraction.test_range_extraction()

