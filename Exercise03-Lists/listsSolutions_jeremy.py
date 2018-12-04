#----------------------------------------------------------------------
# 
# Problem 1
# 
# Create a list containing 100 random integers between 0 and 1000 (use
# iteration, append, and the random module). Write a function called
# average that will take the list as a parameter and return the
# average.
from random import randrange
random_list = []
if len(random_list) <= 100:
    for i in range(0,101):
        i = randrange(0,1001)
        random_list.append(i)
print(random_list)

def average(L):
    result = 0
    for num in L:
        result += num
    new_result = (result/len(L))
    return new_result
print(average(random_list))
    
#----------------------------------------------------------------------
# 
# Problem 2
#
# Write a function sum_of_squares(xs) that computes the sum of the
# squares of the numbers in the list xs. For example,
# sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29.
#
xs = [2,3,4]
def sum_of_squares(alist):
    result = 0
    for num in alist:
        num_squared = num ** 2
        result += num_squared
    return result
print(sum_of_squares(xs))


#----------------------------------------------------------------------
# 
# Problem 3
#
# Write a function sum_of_evens(L) that returns the sum of all the
# even numbers in the list L
# 
def sum_of_evens(L):
    result = 0
    for num in L:
        if num % 2 == 0:
            result += num
    return result
mylist = [1,2,3,4,5,6,7,8]
print(sum_of_evens(mylist))

#----------------------------------------------------------------------
# 
# Problem 4
#
# Write a function count_5(L) that returns the count of how many words
# in the list L have length 5
#
def count_5(L):
    result = 0
    for item in L:
        if type(item) == str:
            if len(item) == 5:
                result += 1
    return result
mylist = ['fourth',3,4,'seven','eight','paper']
print(count_5(mylist))





#----------------------------------------------------------------------
# 
# Problem 5
#
# Write a function replace(s, old, new) that replaces all occurences
# of old with new in a string s:
# Hint: use the split and join methods.

def replace(s, old, new):
    new_string = s.replace(old, new)
    return new_string
s ='I love spom! Spom is my favorite food. Spom, Spom, Spom, yum!'
print(replace(s,"om","am"))


# TESTS -----
# test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
# 
# s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
# test(replace(s, 'om', 'am'),
#        'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')
# 
# test(replace(s, 'o', 'a'),
#        'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')
