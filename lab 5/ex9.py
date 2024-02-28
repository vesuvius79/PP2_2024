import re

def test(pattern, sub, testData, testNumber, expectedResult):
    result = re.sub(pattern, sub, testData)
    print(result)
    
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")

sub = " "
pattern = r"[A-Z]+"

test(pattern, sub, ";';[]'$@^AGMWEjpojIOJIOisss", "test1", ";';[]'$@^ jpoj isss")
test(pattern, sub, "SakenOrazgali", "test2", " aken razgali")
test(pattern, sub, "48964wegewgHOII", "test3", " 48964wegewgH ")
test(pattern, sub, "8946egageagASGS48684", "test3", "8946egageag 48684")