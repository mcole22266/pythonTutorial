def ducklings():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter in ["O","Q"]:
           word = letter + "u" + suffix
        else: 
            word = letter + suffix
        print(word, end = (" "))
    print()

ducklings()

# I needed to be able to run each function individually so i had to 
# create my own strings.py instead of copying your original.

def times_tables():
    import pprint
    n = int(input("What number do you want the times table to go to?"))
    m = list(list(range(1*i, (n+1)*i, i)) for i in range(1,n+1))
    max_width = len(str(m[-1][-1])) +1
    for i in m:
        i = [str(j).rjust(max_width) for j in i]
        print(''.join(i))
times_tables()

# This is some code i pulled from off of a python forum website and I  
# do not fully understand it. I was going to check with you to see if 
# it was somehting you understand or is it over your head as well?