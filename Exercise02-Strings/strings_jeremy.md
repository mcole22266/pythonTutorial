# times_table 

This will cover 3 things:
1. Python's `rjust` attribute 
2. Pretty Print (`pprint`)
3. List Comprehension

## Forum Solution 

For reference, here's the code this markdown file is about:

```python
def times_tables():
    import pprint
    n = int(input("What number do you want the times table to go to?"))
    m = list(list(range(1*i, (n+1)*i, i)) for i in range(1,n+1))
    max_width = len(str(m[-1][-1])) +1
    for i in m:
        i = [str(j).rjust(max_width) for j in i]
        print(''.join(i))
```

### rjust Attribute

As far as your original question, the solution is really complicated because 
it utilizes a `print` attribute (`rjust`) in order to solve it. Essentially, 
what the solution does is get the largest number of characters necessary so 
everything can be spaced out according to that. 

For instance, let's look at the spacing we want for the first three rows and columns: 

```
0  1  2
1  1  2
2  2  4
```

When you break it down, you can imagine that you want each column to have a space 
before the number. This is where the `rjust` attribute comes in handy. The easiest way 
to understand it is to just play with it. Type any string and put a `.rjust(X)` (any 
number in place of the `X`) and you'll see a "right-justified string" of however many 
characters you choose. Python will happily add however many spaces are necessary in order 
to do the proper right-justification.

Try this out in a python terminal: 

```python
name = input('What is your first and last name? ').capitalize()
street = input('What is your street address? ').capitalize()
city = input('What city do you live in? ').capitalize()
state = input('What state do you live in ?(Use abbreviation) ').capitalize()
zip = input('What is your zip? ')

line1 = name.rjust(40)
line2 = street.rjust(40)
line3 = f'{city}, {state} {zip}'.rjust(40)

print(f'''
{line1}
{line2}
{line3}
''')
```

So the solution from the forum essentially figures out the total length of the largest 
character (which would always be the bottom right on the times table), adds one to that 
length to account for spacing between columns, and then right justifies all the values 
according to that length. So, on your regular 12x12 table, the largest value would be 144. 
With 144 being 3 characters long, everything would need to be right-justified to 4 
characters. 

You can learn more about string attributes here: https://docs.python.org/2/library/string.html 

### Pretty Print (`pprint`)

Strangely, the forum solution imports pretty print but never uses it. The line `import pprint` 
just after defining the function imports that module to be used - but it's never used. It's 
possible that the original solution in the forum used it by having `pprint('blahblahblah')` 
which you then turned to `print('blahblahblah')` possibly thinking it was a typo? In any case, 
it presents a good opportunity to talk about a few things. 

First a little background on modules:

#### Modules

Modules are a way to add extra functionality to your coding language by "importing" them. Two 
modules I find myself using quite frequently are Pythons built-in `time` and `random` modules. 
For the sake of simplification, I'll focus on the random module. Feel free to work alongside me 
to play with the module (you may need to restart your python session between each section by 
quitting and opening python/ipython again)

##### Traditional Way 
```python
import random

x = random.random()
```

The random module introduces pseudorandomness in order to simulate random states. In order to use 
that, we need to first import random &rarr; `import random` does that for us. Now, in order to use 
attributes within the random module, we need to call them as such: `random.______`. In the above case, 
we're assigning x to a random value between 0 and 1. This is good for creating probabilitic scenarios. 

For instance, say you're creating a game and there's a 10 percent chance that some event could happen:

```python
import random

def eventOccurs():
    chance = random.random()    #  Chance == random decimal from 0 - 1
    if chance <= 0.10:
        return True             # event occurs
    else:
        return False            # event does not occur
```

If you `eventOccurs()` was triggered 10 times, you would expect ~1 of those 10 would return `True`. 

##### Other Ways

Along the lines of modules, there are other "shortcuts" we can take advantage of. In the above traditional 
case, we may find ourselves typing `random` over and over and over as each call to the random module requires 
`random.______` in order to use a feature. 

The initial example above would be just as valid as such: 

```python
import random as r

x = r.random()
```

What this does is import the entire random module - just as normal - except it does so under a different 
namespacing: `r`. The best way to think of it is just imagining that importing random as a module assigns 
all of its assets to the variable: `random` just as importing everything within the `time` module would 
assign all of its assets to the variable: `time`. When using the syntax `import ________ as _______`, you're 
simply changing the variable that the modules contents are assigned to. 

I find myself doing this so often with `matplotlib.pyplot` &rarr; `import matplotlib.pyplot as plt` - You can 
imagine how much typing that saves in the end when it's called so much in practice.

Now, imagine we instead want to only use a few select things from the module but not the entire thing. I showed 
you an example of this the other day with `random.choice`. Now, you would be perfectly validated in importing the 
module normally and simply using choice as I just mentioned or you could make it even easier. 

`random.choice` is simple - give it a list and it randomly returns one value from that list. Take a second to 
try to figure out what the code below is doing:

```python
from random import choice

def whereToEat(foodChoices):
    return choice(foodChoices)

restaurants = ['McDonalds', 'Krystals', 'Burger King', 'Wendys', 'Pizza Hut', 'Home', 'Subway']

whereToEat(restaurants)
```

What this code does is take the headache out of choosing where to eat and lets Python do it for us. Notice, 
instead of importing the entire random module, we imported one single attribute from it: `choice`. The basic 
syntax for doing this is `from ________ import ________` which makes sense. "**from** this *module* **import** this *attribute*". 

What's cool is that you can even combine the previous two shortcuts. Maybe you don't even feel like typing the 
word choice over and over &rarr; `from random import choice as c` - Now you can say `c(foodChoices)` in order 
to select a single item from foodChoices. Remember, this does affect code readability 

You can learn more about the random module at: https://docs.python.org/2/library/random.html

#### Create your own module

Believe it or not, it's actually quite simple to create your own module. Think about the random module actually 
being a file somewhere that exists called `random.py`. Within that file are a bunch of functions: choice, shuffle, 
random, etc. You can do the exact same thing yourself! 

Simply create any `.py` file with functions inside of it and call it in python. For instance, we can use the 
`makeSum_good.py` file that is in this current directory: (**important**: in order to use your own module, your 
working directory must be the same as the module you want to use.)

```python
import makeSum_good

makeSum_good.makeSum(5, 5)   # should return 10
```

Of course, you could also (more easily) do it as follows:

```python
from makeSum_good import makeSum

makeSum(5, 5)
```

Try it out yourself! Create a file in this same directory called `jeremyModule.py` and create any function you 
want. Then open a python terminal (if you're using VSCode then you can just open a terminal within it) and try 
using the module you created. 

### Pretty Print

We strayed away from Pretty Print but it essentially prettily prints things. I never use it but you can learn about 
it at: https://docs.python.org/2/library/pprint.html  

### List Comprehension

I wanted to add this sort of *advanced* bit just because it's useful and was present in your forum so I at least 
want you to be able to recognize it when you see it. The original forum solution is way up there &uarr; so here it 
is again: 

```python
def times_tables():
    import pprint
    n = int(input("What number do you want the times table to go to?"))
    m = list(list(range(1*i, (n+1)*i, i)) for i in range(1,n+1))
    max_width = len(str(m[-1][-1])) +1
    for i in m:
        i = [str(j).rjust(max_width) for j in i]
        print(''.join(i))
```

On the second to last line, what we see is called **List Comprehension**. It essentially replaces the process 
of creating an empty list and looping through something while appending it to that list with something more concise. 

Here's what you currently know: 

```python
divisibleBy10 = []

for num in range(1000):
    if num % 10 == 0:
        divisibleBy10.append(num)
```

The above code would create a list of all numbers from 0 - 1000 (excluding 1000 itself) that are 
divisible by 10. With list comprehension, it would be equally created as follows:

```python
divisibleBy10 = [num for num in range(1000) if num % 10 == 0]
```

Try reading the above code and working the logic out in your head. The best way to understand 
list comprehension is to just see a bunch of examples:

- A list of all numbers from 1 - 10 squared:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbersSquared = [num**2 for num in numbers]
```

  - You could just as easily have done it all on one line as well

  ```python
  numbersSquared = [num**2 for num in range(1, 11)]
  ```

- The square of all numbers divisible by 10:

```python
numbersSquaredAndDivisibleBy10 = [num**2 for num in range(1000) if num % 10 == 0]
```

You can find more information about List Comprehension here: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
