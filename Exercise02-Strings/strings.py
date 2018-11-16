#----------------------------------------------------------------------
# 
# Problem 1
# 
# In Robert McCloskey’s book Make Way for Ducklings, the names of the
# ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and
# Quack. This loop tries to output these names in order.
# 
# prefixes = "JKLMNOPQ"
# suffix = "ack"
# 
# for p in prefixes:
#     print(p + suffix)
# 
# Of course, that’s not quite right because Ouack and Quack are
# misspelled.
#
# Create a function, called ducklings, that prints out the correct
# names for the ducklings

def ducklings():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

#----------------------------------------------------------------------
# 
# Problem 2
#
# Create a function, called twelve_table, that prints out a neatly
# formatted multiplication table, up to 12 x 12.
#

def twelve_table():


#----------------------------------------------------------------------
# 
# Problem 3
#
# Write a function, called reverse_string, that reverses its string
# argument.
# 

def reverse_string(string):


#----------------------------------------------------------------------
# 
# Problem 4
#
# Write a function, remove_letter, that removes all occurrences of a
# given letter from a string.
#

def remove_letter(string, removeChar):


#----------------------------------------------------------------------
# 
# Problem 5
#
# Write a function, count_substring, that counts how many
# non-overlapping occurences of a substring appear in a string. Takes
# two parameters, a string and a substring to count

def count_substring(string, substring):


# FOR TESTING ---------------------------------------------------------
# ---------------------------------------------------------------------
# Problem 1:
assert ducklings() == 'Jack Kack Lack Mack Nack Ouack Pack Quack'

# Problem 2:
print('Should be a multiplication table: 12x12')
twelve_table()

# Problem 3: 
assert reverse_string('Hello World') == 'dlroW olleH'
assert reverse_string('12345') == '54321'

# Problem 4: 
assert remove_letter('Hello World', 'l') == 'Heo Word'

# Problem 5:
assert count_substring('Bippity Boppity Boo', 'pity') == 2
