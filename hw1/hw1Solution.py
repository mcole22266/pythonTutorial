print("I will now count my chickens")     # Syntax: missing parenthesis

# Only modify the operators in these two lines
print("Hens", 25 + 30 / 6)                # Semantic: should equal 30
print("Roosters", (100 - 95) * 3)           # Semantic: should equal 15



print("Now I will count the eggs:")

eggs = 500
print(eggs)                               # Runtime: naming error



print("Is it true that 3 + 2 < 5 - 7?")

# Only modify operators here
print(3 + 2 > 5 - 7)                      # Semantic: should print False

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")



print("How about some more.")              # Syntax: missing quote

test1 = 5 > -2
print("Is it greater?", test1)             # Runtime: name error
test2 = 5 >= -2
print("Is it greater or equal?", test2)
test3 = 5 <= -2
print("Is it less or equal?", test3)       # Syntax: missing comma
