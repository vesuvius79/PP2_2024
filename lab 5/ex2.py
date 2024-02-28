import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern,testData) == expectedResult:
        print(f"{testNumber} is passed!")
    elif re.search(pattern,testData) != None:
        print(f"{testNumber} is passed!")
    else:
        print(f"{testNumber} is not passed!")

pattern = r"ab{2,3}"

test(pattern, "aaaaaasdsgsdsaabbb", "test1", True)
test(pattern, "wafafaadwrwgabb", "test2", True)
test(pattern, "apogjwepogjwpoegb", "test3", False)