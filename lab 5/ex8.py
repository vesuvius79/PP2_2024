import re

def test(pattern, testData, testNumber, expectedResult):
    obj = re.split(pattern, testData)
    result = ""
    for x in obj:
        if x != "":
            result += x
    print(result)
    
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
         print(testNumber + " is not passed!")

    
pattern = "[A-Z]"

test(pattern, "SakenKbtu", "test1", "akenbtu")
test(pattern, "HAHAHAlowwwwJKJK", "test2", "owwww")
test(pattern, "12OPPO111", "test3", "12111")
test(pattern, "8771AAa", "test4", "8771Aa")