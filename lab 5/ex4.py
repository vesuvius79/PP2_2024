import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(f"{testNumber} is passed!")
    elif re.search(pattern, testData) != None:
        print(f"{testNumber} is passed!")
    else:
        print(f"{testNumber} is not passed!")



pattern = r"[A-Z][a-z]+"

test(pattern, "ArsenMiramzhanuly", "test1", True)
test(pattern, "aaaFgagegRWHHaa", "test2", True)
test(pattern, "AAAAAAAAAA", "test3", False)