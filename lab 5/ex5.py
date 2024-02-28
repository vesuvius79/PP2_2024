import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) != None:
        print(f"{testNumber} is passed!")
    else:
        print(f"{testNumber} is not passed")


pattern = r"a.*b$"

test(pattern, "12a%^&*  b", "test1", True)
test(pattern, "@@@a_  _+bm", "test2", None)
test(pattern, "``;::a}{89ahjhjhjb", "test3", True)