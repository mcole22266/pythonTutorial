# HW2 - Strings 

## Assignment 
The first assignment is called `strings.py`. In this assignment, you'll find instructions 
written as comments that explain what to do for each problem. You need to create the function 
and then, underneath, call that function and have it demonstrate what was instructed. 


An example would look something like:    
```python
# Problem 1
# Create a function that takes two numbers as parameters and returns their sum
# ----------------------------------------------------------------------------
def makeSum(num1, num2):
    total = num1 + num2
    return total

makeSum(42, 8)   # should return 50
```

## Instructions
1. Copy the assignment into a different file:
 - `cp strings.py stringsSolution.py`
2. Solve the assignment
3. Push the assignment up and let me know you're done
 - `git add stringSolution.py`
 - `git commit -m 'Completed stringSolution.py'`
 - `git push`

## Note:
At the bottom, I've created some tests using **assertion statements**. These are a really 
good thing to eventually learn as you can premptively create tests for desired effects in 
your code and test yourself. They help alot with preventing **Semantic Errors**. i

At this point, you may not know what they do. But, you can still make use of them by looking 
at them and seeing what answer you should expect each function to return. Also, when you run 
your code, if you see `Assertion Error`, it means your code is working but isn't returning the 
correct thing. 

With the example above, I'll demonstrate how an assertion statement is used:
```python
def makeSum(num1, num2):
    total = num1 + num2
    return total

assert makeSum(4, 3) == 7
assert makeSum(42, 8) == 50
```
