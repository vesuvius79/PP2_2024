import re

def test(pattern, sub, testData, testNumber, expectedResult):
    result = re.sub(pattern, sub, testData)
    print(result)
    
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")
        
pattern = r"[\s,\.]"
sub = r":"

test(pattern, sub, "Saken Proga", "test1", "Saken:Proga")
test(pattern, sub, " kbtua, flllfe  aaa", "test2", ":kbtua::flllfe::aaa")
test(pattern, sub, "+771 065 45 45, ", "test3", "+771::065:45:45::")