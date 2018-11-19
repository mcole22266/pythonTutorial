# When run, this assertion statement will not fail

def makeSum(num1, num2):
    total = num1 * num2    # NOTE the desire is to add 2 numbers yet this gets the product of those two
    return total 

assert makeSum(42, 8) == 50
