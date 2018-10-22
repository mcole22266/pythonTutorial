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

Go ahead and create the above code in Atom, save it as `hello.py` and then run it in 
GitBash by typing `python hello.py`. 

Notice that the `input` function acts very similarly to the `print` function except it 
allows a user to type something which is then saved into whatever variable you like 
(in the above case, the user input was assigned to a variable called `name`. 

## Assignments
Below are a few assigments to help you become familiar with the `input` function that 
will also challenge you based on what you know at this point:

### Example
First I want to walk you through an example. We're going to make a program that adds two 
numbers together.

1. Create a file called 'example.py' and open it with Atom &rarr; `atom example.py`
2. First, let's print something to let the user know that they're running a program
 - `print('Welcome to Number Adder 3000: Pro Edition')`
 - `print('-----------------------------------------')` (this line to make it pretty)
3. Now lets let the user give you two numbers using the `input` function and assign them 
to some variables:
 - `number1 = input('Number 1:  ')`
 - `number2 = input('Number 2:  ')`
4. Now that we have the user's numbers assigned to variables, we need to get the total:
 - `total = number1 + number2`
5. Now simply finish off by printing the answer to the screen.
 - `print('Total: {}'.format(total))`
6. Now save the program in Atom and run in in Git Bash. You should see something like this:

```bash 
$ python example.py
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
total = number1 + number 2

print(f'Total: {}'.format(total))
```

### Part A: Fahrenheit &rarr; Celsius 
The goal here is to make a program that converts Farenheits to degrees. I'll walk you 
through it.

1. First create a file called `converter.py` and open it with Atom &rarr; `atom converter.py`
2. On the first line, use the `input` function in order to ask the user for the a 
temperature in Fahrenheit and save it into a variable called `f`. 
3. On the next line, we want to convert fahrenheit into celsius so Google the formula. 
 - `c = whateverTheFormulaIs` will assign the conversion to a variable called `c`. 
4. Finally, we want to print the answer to the screen (maybe use the `format` function you 
recently learned?

Here are some sample runs that should be similar to yours:
```bash
$ python converter.py
Enter temperature in Fahrenheit: 32
The temperature in Celsius: 0.0

$ python converter.py
Enter temperature in Fahrenheit: 72
The temperature in Celsius: 22.222222222
```

**Bonus:** Maybe you can think of a way to format (or round *hint hint*) the value so that 
you the floating point doesn't stretch out so far.


### Part B: Area of a Trapezoid
Create a new program called `trapezoidArea.py` that will ask the user for the information needed 
to find the area of a trapezoid and then print the area. Here is the formula to find the area 
of a trapezoid:    

`0.5 * height * (bottomLength + topLength)`

Sample Run should look something like:

```bash
$ python trapezoidArea.py
Enter the height of the trapezoid: 5
Enter the length of the bottom base: 10
Enter the length of the top base: 7
The area is: 42.5
```
