"""
    pytest ews/ews_interview_test.py
"""
def fun(input):
    result = ""
    index = 0
    count = 1
    letter = input[index]
    while index < len(input):
        deb = f"{index=}{count=}{letter}"
        # print (deb)
        if index == len(input) -1:
            result = result + f"{letter}{count}"

            break
            # result = result + f"{letter}{count}"

        if letter == input[index + 1]:
            count+= 1
        else:
            result = result + f"{letter}{count}"
            # print (result)
            letter = input[index + 1]
            count = 1
        
        index+=1
    
    return result


def test_fun():
    cases = {
        "aabbba": "a2b3a1",
        "a": "a1",
        "aa": "a2",
        "ab": "a1b1",
    }
    for input, expected_output in cases.items():
        actual_output = fun(input)
        assert expected_output == actual_output
