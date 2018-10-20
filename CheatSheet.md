# Cheat Sheet

## Data Types

|   type   |   shorthand   |            Example                |
|:--------:|:-------------:|:---------------------------------:|
| Integer  |     `int`     |              42                   |
|  Float   |    `float`    |             1.21                  |
|  String  |     `str`     |         "Hello World"             |
|   List   |    `list`     | [42, 1.21, "foo", [1, "bar"], 5]  |
|  Tuple   |    `tuple`    |     (3, 2) *can contain anything* |
|Dictionary|     `dict`    |    {'Red': 'rojo', 'Eggs': 14}    |

### Integer
- contains no decimal place
- can convert a "number-like object" to an integer using `int()`
 - especially helpful when using `input()` function
 - when converting a float to an int - number is not rounded but merely "chopped off" 
 at the decimal
- Ex:

```python
x = '5'      # x == string
x = int(x)   # now x has been converted to an integer

# Another case
moneyInWallet = input('How much money do you have? ')  # user will input but input is a string
moneyInWallet = int(moneyInWallet)   # now converted to integer rather than string
```

### Float
- if there is a decimal, it's a float. 
- can convert a "number-like object" to a float using `float()`
 - if the number is an integer it will go from `10` &rarr; `10.0` for example

### String
- placed between single quotes `'hello'`, double quotes `"hello"`, or triple quotes `'''hello'''`
- immutable
- can consist of any characters
- **using the `input()` function will always return a string**

### List
- can contain any datatype (or even a mix of datatypes)
 - can also "nest" lists by putting lists inside of lists
 - or even dictionaries or tuples within lists
 - Ex: `myList = ['Hello world', 42, ['another list', 1.21], {'dictionary': 'here'}, ('tuple', 'here')]`

### Tuple
- similar to lists except immutable
- useful in **tuple unpacking** where multiple values can be assigned to multiple variables in one line.

### Dictionary
- key-value pair
- **unordered**
- written as `{key1: value, key2: value}` but usually formatted for readability as in the example 
below:

```python
englishToSpanish = {'red': 'rojo',
                    'blue': 'azul',
		    'water': 'agua',
		    'one': 'uno'}
```

- **Note**: dictionary values can also be other dictionaries 

---

### Functions
Basic method to **create** and **call** functions:

```python
# first create the function
def hello():
    return 'Hello world'

hello()   # then call the function - this will print Hello world
```

However adding a bit of complexity makes functions far more useful:
- inside of the parenthesis, you can add **parameters** which can be used within the function
- Say you want to create a simple function that adds two numbers together

```python
# first create the function but include parameters inside of parenthesis
def addTwoNumbers(number1, number2):
    total = number1 + number2         # this line adds the two numbers given to the function
    return total                      # this line returns that number 

addTwoNumbers(3, 4)   # this would return 7
```

In the example above, when the function was called (`addTwoNumbers(3, 4)`) here's what happened:
1. `3` &rarr; `number1`
2. `4` &rarr; `number2`
3. `total = number1 + number2` &rarr; `total = 3 + 4`
4. `total` &rarr; `7`
5. `return total` &rarr; `return 7`


