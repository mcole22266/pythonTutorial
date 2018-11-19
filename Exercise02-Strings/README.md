# Strings 

## Assignment 
In the file `errors.py`, you'll find instructions written as comments that explain what to do for each problem. 
You may find it helpful to go ahead and create some **assertion statements** in order to test your code 
while it's being created. 

An example would look something like:    
```python
# Problem 1
# Create a function that takes two numbers as parameters and returns their sum
# ----------------------------------------------------------------------------
def makeSum(num1, num2):
    total = num1 + num2
    return total

assert makeSum(42, 8) == 50
```

An assertion statement (as seen on the last line) will evaluate to either a `True` or a `False`. In the above 
example case, this would evaluate to `True` so, when running the code, you wouldn't even notice that line is 
there. However, were it to evaluate to `False`, you would get an `AssertionError` in your code. To demonstrate, 
I've created two files: `makeSum_good.py` and `makeSum_bad.py`

Notice that running the `makeSum_bad.py` file returns an `AssertionError`:

```
$ python makeSum_bad.py

Traceback (most recent call last):
  File "makesum_bad.py", line 7, in <module>
    assert makeSum(42, 8) == 50
AssertionError
```

You can see how beneficial this can be when writing code. It allows you to go ahead and "Assert" what you want 
the function to do then helps you *catch* when that function does the wrong thing. If you run the `makeSum_good.py` 
file, you'll see that it does as asked and nothing is returned.  

Of course, you don't *have* to use Assertion Statements when writing code but it is often more beneficial to 
start there before you even start writing code. For example, if you were writing the above makeSum program, 
you may start like this:

```python
def makeSum():
    pass

makeSum(4, 10) == 14
makeSum(-5, 2) == -3
makeSum(0, 0) == 0
```

When you first run it, it will obviously fail but, in doing it this way, you're already thinking about all the 
cases in which a makeSum function may fail. What happens if both numbers are zero? What happens if one number is 
a negative? What about if both are? These are the ways you end up preparing yourself by using Assertion Statements.

## Instructions

1. Copy `errors.py`
 - `cp errors.py errorsSolution_yourname.py
2. Open the copy in your favorite text editor and solve the problems 
3. When complete, push back up to the repo:
 - First add the file to the staging area:
 	- `git add errorsSolution_yourname.py`
 - Then commit your changes with a useful message
 	- `git commit -m 'Completed errorsSolution_yourname.py'`
 - Push your changes up to the repo
 	- `git push`
4. Let me know when you're done and I can check your work.
