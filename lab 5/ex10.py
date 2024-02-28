import re


def replace(match):
    return f"{match.group().lower()[0]}_{match.group().upper()[1]}"

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, replace, testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")

pattern = r".[A-Z]"

test(pattern, "SakenKbtu", "test1" ,"Saken_Kbtu")
test(pattern, "sakenProga", "test2", "saken_Proga")
test(pattern, "_____2$&$Kbtu_pp2_top, ", "test3", "2$&$KbtuPP2top")