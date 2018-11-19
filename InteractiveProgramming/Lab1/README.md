# Lab 1: Custom Calculators 
The point of this lab is to create simple programs that make a task easier by:
1. Taking in data
2. Performing calculations
3. Outputting data

A good way to do this is by using the `input()` command in order to save a user's input 
as a variable. For instance, suppose you want to write a program that says hello to the 
user. It would look as follows:

```python
name = input('Please type your name.  ')

print('Hello {}!'.format(name))
``` 

Go ahead and create the above code in your preferred text editor, save it as `hello_yourname.py` and then run it in 
GitBash by typing `python hello_yourname.py`. 

Notice that the `input` function acts very similarly to the `print` function except it 
allows a user to type something which is then saved into whatever variable you like 
(in the above case, the user input was assigned to a variable called `name`. 

## Assignments
Below are a few assigments to help you become familiar with the `input` function that 
will also challenge you based on what you know at this point:

### Example
First I want to walk you through an example. We're going to make a program that adds two 
numbers together.

1. Create a file called 'example.py' and open it with your preferred text editor &rarr; `atom example.py`
2. First, let's print something to let the user know that they're running a program
 - `print('Welcome to Number Adder 3000: Pro Edition')`
 - `print('-----------------------------------------')` (this line to make it pretty)
3. Now lets let the user give you two numbers using the `input` function and assign them 
to some variables:
 - `number1 = input('Number 1:  ')`
 - `number2 = input('Number 2:  ')`
4. **Important**: This is the part that alot of programmers miss. When you assign a variable 
using the `input` function, the user input is **always** given as a **string** - even if you 
want it to be an integer or float. To solve this, we need to convert our new variables into 
integers (or floats) before we do any arithmetic.
 - `number1 = int(number1)`
 - `number2 = int(number2)`
5. Now that we have the user's numbers assigned to variables and of the correct type, we 
need to get the total:
 - `total = number1 + number2`
6. Now simply finish off by printing the answer to the screen.
 - `print('Total: {}'.format(total))`
7. Now save the program in your preferred text editor and run in in Git Bash. You should see something like this:

```bash
$ python example_yourname.py
Welcome to the Number Adder 3000: Pro Edition
---------------------------------------------
Number 1: 55
Number 2: 500
Total: 555
```

Now you've completed the program! Here is the entire code in case you get stuck:

```python
print('Welcome to Number Adder 3000: Pro Edition')
print('-----------------------------------------')

number1 = input('Number 1:  ')
number2 = input('Number 2:  ')

number1 = int(number1)
number2 = int(number2)

total = number1 + number2

print('Total: {}'.format(total))
```
*\- Note: the spacing is readability and is not needed for Python to run \-*

Now, go ahead and run your code to make sure it works. Can you think of any ways that the 
user could cause an error with your programming? Later, you'll learn ways to guard against that 
and ensure that the user doesn't break your program.

### Part A: Fahrenheit &rarr; Celsius 
The goal here is to make a program that converts Farenheits to degrees. I'll walk you 
through it.

1. First create a file called `converter_yourname.py` and open it with your preferred text editor.
2. On the first line, use the `input` function in order to ask the user for the a 
temperature in Fahrenheit and save it into a variable called `f`. 
3. Remember that user-input is always a string. We need to perform some arithmetic on the given 
number so be sure to convert it from a string into an integer (or float)
4. On the next line, we want to convert fahrenheit into celsius so Google the formula and see if 
you can figure out how to do it.
 - `c = whateverTheFormulaIs` will assign the conversion to a variable called `c`. 
 - **Note:** If you can't figure it out, I've gone ahead and included the line at the very bottom of 
 this document.
5. Finally, we want to print the answer to the screen (maybe use the `format` function you 
recently learned?

Here are some sample runs that should be similar to yours:
```
$ python converter_yourname.py
Enter temperature in Fahrenheit: 32
The temperature in Celsius: 0.0

$ python converter_yourname.py
Enter temperature in Fahrenheit: 72
The temperature in Celsius: 22.222222222
```

**Bonus:** Maybe you can think of a way to format (or **round** *hint hint*) the value so that 
you the floating point doesn't stretch out so far.


### Part B: Area of a Trapezoid
Create a new program called `trapezoidArea_yourname.py` that will ask the user for the information needed 
to find the area of a trapezoid and then print the area. Here is the formula to find the area 
of a trapezoid:    

`0.5 * height * (bottomLength + topLength)`

Sample Run should look something like:

```bash
$ python trapezoidArea_yourname.py
Enter the height of the trapezoid: 5
Enter the length of the bottom base: 10
Enter the length of the top base: 7
The area is: 42.5
```

### Part C: Mad Libz
Create a program called `madlibz_yourname.py` that asks the user for adjective, nouns, verbs, adverbs, 
name of a person they know, number, color, feeling, etc.. in order to gather information to fill 
out a fun Mad Libz story. 

## When Complete
When you've completed everything, push everything up to Github:
1. Add all new and changed files to the staging area:
 - `git add hello_yourname.py example_yourname.py converter_yourname.py trapezoidArea_yourname.py madLibz_yourname.py` 
2. Commit your changes with a message explaining what the commit is for:
 - `git commit -m 'Completed Interactive Lab 1'`
3. Push your commmitted changes up:
 - `git push`

---
#### formula for converter_yourname.py
`c = (f - 32) * (5/9)`
