from random import randrange
name = input('What is your name?   ')
num = randrange(1,101)
guess_counter = 0
print('Hello ', name,'. I am going to give you 10 chances to guess the number I am thinking of.')
while guess_counter <= 10:
    guess = int(input("Take a guess between 1 and 100.   "))
    if guess > num:
        if (guess - num) < 10:
            print('Your guess is warm!')
        elif (guess - num) > 10:
            print('Your guess is cold!')
        print('Your guess is to high.')
        guess_counter += 1
    if guess < num:
        if (num-guess) < 10:
            print('Your guess is warm!')
        elif (num - guess) > 10:
            print('Your guess is cold!')
        print('Your guess is to low.')
        guess_counter += 1
    if guess == num:
        guess_counter += 1
        break
while guess_counter > 10:
    print("Sorry, ", name, "you have exceeded your number of guesses. My number was ", num".")
    break
if guess == num:
    print("Gongratulations", name," it only took you", guess_counter," guesses to guess that the number was", num,".")