import re

def repl_func(match):
    return match.group()[1].upper()

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, repl_func, testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")

pattern = r'_.'

test(pattern, "Saken_Pp", "test1" ,"SakenPp")
test(pattern, "kbtu_pp", "test2", "kbtuPp")
test(pattern, "_____2$&$Kbtu_pp2_top, ", "test3", "2$&$KbtuPP2top")