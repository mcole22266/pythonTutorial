# When run, this assertion statement will not fail

def makeSum(num1, num2):
    total = num1 + num2
    return total 

assert makeSum(42, 8) == 50
