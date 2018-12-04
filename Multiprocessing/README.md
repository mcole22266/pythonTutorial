# MultiProcessing

This markdown file will cover a few ideas:
- CPU Usage
- MultiProcessing
- Using the time module to time events

## Setup

For simplicity's sake, I used iPython for this. Because of that, I encourage you to 
do the same and work alongside me throughout this. If you have a second monitor, it 
may make things easier to put your System Monitor (we'll discuss what that is in a 
second) on your second screen. If that's not available, then I recommend being sure 
that it's visible before running the commands that you'll be given to make your 
system do work. 

#### System Monitor

The System Monitor is a way you can view, in real time, various aspects of your 
hardware. Currently, I'm using Linux Mint and have a CPU History graph, Memory and 
Swap History graph, and a Network History graph. 

You can access your System Monitor in different ways depending on your particular 
Operating System. Here are the ways for three different OS's:

- **Linux Mint**:
 - Open your menu and type 'System Monitor' in the search bar. 
 - At the top of the Window, click the 'Resources' tab
- **Windows**:
 - Access your Task Manager: `ctrl+alt+del` &rarr; click 'Task Manager'
 - Click the 'Performance' tab
 - Click CPU
 - If it's not already showing all cores, right click on the graph and click on 
'Change graph to' then select 'Logical Processors'
- **Mac**:
 - -- *Add Later* -- 

#### iPython

Open iPython and follow along with the code examples in this file.

## Exercise 

### Get Started

With the aim of this exercise being to really push your cpu to its limits, we're 
going to need to create some work for your computer to do. What I find to be a 
pretty decent workload is to ask Python to take a list of numbers and square them 
all to their own power and then return that list. Let's make a function that does 
that so we can use it repeatedly:

```python
def exponentiate(aList):
    exponetiatedList = []
    for num in aList:
        exponentiatedList.append(num**num)
    return exponentiatedList
```

Simple enough.. now let's see this function in action - **keep an eye on your 
System Monitor when you run this**

```python
exponentiate([1, 2, 3, 4, 5])
```

You likely didn't see even the smallest peak from your System Monitor - the task we gave 
to Python was actually quite small. The ultimate aim in this exercise is going to be to 
create a huge 'Big List' filled with a bunch of smaller 'Mini Lists' in order for your 
computer to have quite a few tasks to accomplish. Let's create this now:

```python
# Mini List will have 2,000 integers:
miniList = list(range(1000, 3000))

# Big List will have 25 Mini Lists
bigList = []
for _ in range(25):
    bigList.append(miniList)

# - Let's go ahead and test out our work on a single Mini List - 
exponentiate(miniList);  # add a semicolon to suppress output as we don't care about 
                         # the actual output
```

Notice that even with 2,000 numbers, your processor can easily handle creating a new 
list where every single number is raised to its own power. **Bask in that power**. 

### Creating a Timer

Now, we want to create a timer so we can easily see how long it takes to process 
these upcoming tasks. There are tons of ways to create timers - lots more fluid than 
what we're about to do - but we're just going to hack something together using time 
from the time module and some simple math:

```python
from time import time

time()
```

Notice that what `time()` returns is a float of seconds. Do the following to create a 
very simple timer:

```python
start = time()

# wait a few seconds before continuing...
end = time()

f'{end-start} sec'
```

Simple! You should have gotten the number of seconds that you took to wait. This is 
exactly what we'll do and is, in principle, exactly how you create timers in Python. 

Now, let's actually put this into practice and do our first real test. One issue 
with using iPython for this is that Python will immediately begin executing code the 
moment you hit Enter. We need some way to force multi-lines into iPython before allowing 
it to begin processing. Fortunately, there's a keyboard shortcut for that! Similar to 
using `ctrl+l` in order to clear the screen or using `ctrl+c` as a keyboard interrupt, 
you can force iPython to add a new line with `ctrl+o`. In the following, I find 
myself typing the first line and, instead of hitting enter, type `ctrl+o` to force a 
new line. After that, I can continue to add line after line of code. It isn't until I hit 
`Enter` on a blank line that Python will begin executing what you've typed. 

With that, let's give our first big task to Python:

```python
new = []

start = time()   # Dont' forget to use ctrl+o to force a new line here
for mList in bigList:
    new.append(exponentiate(mList)
end = time()
f'{end-start} sec'
```

You should have noticed that this may have taken some time (~3 seconds on my computer) and, if 
you happened to keep an eye on your System Monitor, you likely saw it peak a bit. If you didn't, 
no worries, we're going to run it a couple more times to sort of get a mental average of how well 
performs. Using the up and down arrows, you can cycle through previous terminal entries. You'll 
find this to be extremely useful in saving time. For instance, rather than re-type everything you 
just did, simply hit the up arrow and then enter! Do it a few more times.

My results hovered around 3 seconds each time - all of your results should also have stayed 
roughly the same each time. Clearly, this isn't enough work to really get to see the results of what 
we plan to do. **We need more work**. Let's create a new **larger** Mini List and append that to our 
Big List. The results will be a much bigger workload for our computer:

```python
miniList2 = list(range(1000, 5000))  # miniList was 1000-2000

for _ in range(25):         
    bigList.append(miniList2)
```

Now our Big List is twice the size as it was before **and** the latter half of the Big List is filled 
with much larger Mini Lists than the first half. Let's go ahead and see how much this has affected our 
workload. Either type the following or press up to go back to it and hit Enter (keep an eye on your 
System Monitor for this one):

```python
start = time()   # Dont' forget to use ctrl+o to force a new line here
for mList in bigList:
    new.append(exponentiate(mList)
end = time()
f'{end-start} sec'
```

Notice the effects of an increased workload. You should have definitely noticed that it took much longer 
and you should have noticed that your cpu utilizations jumped up for much longer! But, hopefully you still 
noticed how much extra work your processor had room for. This is what we hope to address!

### Concept

What Python is doing by default is assigning a single job at a time to any cpu who is available. In 
this particular case, it's grabbing a Mini List from the Big List, telling a processor how and what 
to process, waits for it to complete, grabs another miniList, passes it to an available processor, etc..

Just imagine you're the manager of some company and you need the office cleaned. You have several workers 
on hand but, for some reason, you tell one guy to clean the bathroom. When he returns, you send someone else 
to the warehouse. When he returns, you send another to clean the receptionist area. When he returns, 
you send someone to the break room. Clearly, you would have had everything cleaned had you simply sent each 
worker to a each room to clean simulataneously. This is our goal! We have a single job (Take a list and 
'exponentiate it', then give it back). We can do this by creating a pool of workers - each being processors - 
and giving them the Big List with the goal of grabbing each Mini List and exponentiating them until all are 
done. 

But, before we dive into that, we should get introduced to the built-in `map` function as it is quite similar.

### `map`

Let's take a look at something we did earlier:

```python
new = []
for mList in bigList:
    new.append(exponetiate(mList))
```

Notice that before what we had to do was create a new list - `new = []` - then loop through a the Big List, 
assigning each list to `mlist` - `for mList in bigList:` - then we appended each result to the new list - 
`new.append(exponetiate(mList))`. 

There's not necessarily anything wrong with that but there's a much simpler way to accomplish the exact same 
thing. Try out the following:

```python
new = list(map(exponentiate, bigList))
```

Let me break down what that does. Let's just look at the map function itself: `map(exponentiate, bigList)`. 
Map is, itself, a function that takes two arguments: a function to map onto an iterable, and an iterable. 
What this particular mapping is effectively doing is mapping the idea of exponentiation onto our list of lists. 

To better understand it, let's create something a bit more simplified:

```python
# First let's create a simple hello function
def hello(name):
    return f'Hello {name}!'

# Next, let's create a list of people to say hello to
nameList = ['Rachel', 'Phoebe', 'Monica', 'Ross', 'Chandler', 'Joey']

# Now, let's say hello to all of them by mapping the hello function onto the nameList
map(hello, nameList)
```

Notice that it returned something that was likely unexpected: a Map Object. We can do different things with 
map objects but it is more relevant in this context that we return a list of these greetings.

```python
list(map(hello, namelist))
```

There we go! If we wanted to use this list in the future, we could simply save it into a variable just as 
we do above when exponentiating the Big List into the new list. 

### Multiprocessing

Due to limitations with how multiprocessing works in Windows, we're going to change up the workflow a bit. 
The issue in Windows has to do with how Windows handles passing tasks off simultaneously and, in short, it 
requires that `if __name__ == '__main__:'` is used (which can only be used in a script). With that said, open 
your favorite text editor and create a file called `multi_yourname.py` and type (or copy and paste if you're 
a lazy bum) the following code. 

```python
# First, let's recreate what we've done before

from time import time

miniList = list(range(1000, 3000))
bigList = [miniList for _ in range(25)]  # handy use of list comprehension

miniList = list(range(1000, 5000))
bigList = [miniList for _ in range(25)]

def exponentiate(aList):
    print('Exponentiating a List')  # Let's add print statements so we'll know what our program is doing 
    newList = [num**num for num in aList]
    print('Completed exponentiation')
    return newList 

if __name__ == "__main__":
    start = time()
    newList = list(map(exponentiate, bigList))
    end = time()

    # Let's add some feedback so we know how long it took. 
    print()
    print('Done')
    print()
    print(f'It took {end-start} seconds to complete this task')
```

Go ahead and run the code above. You should see similar results as you did last time. We're now going to 
begin modifying this code to be better suited for multiprocessing. First, we'll need to import the module. 
You don't want to repeatedly type `multiprocessing` over and over so add a line to the beginning the 
the file: `import multiprocessing as mp`. 

Now, because everyone's setup is different, let's use this module to go ahead and grab the maximum number 
of workers that are available to us. Let's add that line and also add a line asking the user how many 
workers they'd like to use. Here's a snippet of the code:

```python
# ...
if __name__ == "__main__":
    maxCPU = mp.cpu_count()
    numCPU = input('How many workers would you like to use? ')

    start = time()
#    ...
```

The way multiprocessing works is by creating a pool of workers like so `numWorkers = mp.Pool(X)` - inserting 
the number of workers you'd like where the X is. Since this is a script to be used for demonstration purposes, 
it'll be really useful to allow you to choose how many workers to use so you can compare your results. Here 
are some considerations:

- What might you do in order to make it easier for the user to choose to use the max amount?
- What if the user tries to ask for more workers than his cpu has available? How can you prevent this?

Think about those things before moving on. The code in this next section is a snippet of changes you should make 
that aim to solve these questions. 

```python
# ...
if __name__ == "__main__":
    maxCPU = mp.cpu_count()
    numCPU = input('How many workers would you like to use? (input `max` to use all available workers). ')
    if numCPU.strip().lower() == 'max':  # allow the user to simply say max to use all workers
        numCPU = maxCPU
    else:
        numCPU = int(numCPU)  # turn user input into an integer 
        if numCPU > maxCPU:   # Now block the user from using too many processors
            numCPU = maxCPU
# ...
```

This code can still be broken by a user, but it will suffice for our purposes. Now, let's actually call the 
multiprocessing module to do what it was meant to do. First a pool of workers needs to be made, then we 
need to use that pool to map bigList onto exponentiate (similar to before). 

```python
# ...
        if numCPU > maxCPU:
            numCPU = maxCPU

    workers = mp.pool(numCPU)  # create the pool of workers
    start = time()
    newList = workers.map(exponentiate, bigList)  # use the map attribute of your pool of workers 
    end = time()

    print()
    print('Done')
    print()
    print(f'It took {end-start} seconds for {numCPU} cpus to complete this task.')
```

Now, your code should be complete! If needed, before moving on, I'll supply the entire file:

```python
import multiprocessing as mp
from time import time 

miniList = list(range(1000, 3000))
bigList = [miniList for _ in range(25)]

miniList = list(range(1000, 5000))
bigList = [miniList for _ in range(25)] 

def exponentiate(aList):
    print('Exponentiating a list')
    newList = [num**num for num in aList]
    print('Completed exponentiation')
    return newList 

if __name__ == "__main__":
    maxCPU = mp.cpu_count()
    numCPU = input('How many workers would you like to use? (input `max` to use all available workers).  ')
    if numCPU.strip().lower() == 'max':
        numCPU = maxCPU
    else:
        numCPU = int(numCPU)
        if numCPU > maxCPU:
            numCPU = maxCPU 


    workers = mp.Pool(numCPU)
    start = time()
    newList = workers.map(exponentiate, bigList)
    end = time()
    
    print()
    print('Done')
    print()
    print(f'It took {end-start} seconds for {numCPU} cpus to complete this task.')
```

Now, make sure you're looking at your System Monitor. First, run the program and tell it you'd like to only use 
1 cpu. Compare that to the results of 2 cpus. Then, go ahead and max it out. You should see your cpu usage 
skyrocket to 100% and notice the time to completion is much much faster. 

Here are my results for comparison:

- Linux Mint desktop running on the Ryzen 7 2700x (16 workers available)
 - 1 Worker: 13.55 seconds
 - 4 Workers: 3.96 seconds
 - 8 Workers: 2.48 seconds
 - 16 Workers: 2.08 seconds

- Windows 10 desktop running on the Ryzen 7 2700x (16 workers available)
 - 1 Worker: 17.76 seconds 
 - 4 Workers: 4.91 seconds
 - 8 Workers: 3.27 seconds
 - 16 Workers: 2.55 seconds

- Windows 10 laptop running on the Intel Core i7 8th gen (8 workers available)
 - 1 Worker: 19.82 seconds
 - 4 Workers: 7.57 seconds
 - 8 Workers: 6.10 seconds

If you think your computer can handle it, change the code to make the program work even harder! Make the miniLists 
even larger or add more of them to the bigList. See how this changes the rate of completion!
