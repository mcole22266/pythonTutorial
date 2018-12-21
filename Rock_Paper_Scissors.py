from random import choice

def play():
    player = input('Would you like to play Rock, Paper, Scissors?')
    player = player.lower()
    if player == 'yes':
        return True
    else:
        return False

mylist = ['Rock','Paper','Scissors']




while play() == True:
    computer = choice(mylist)
    computer = computer.lower()

    player = input('Which one would you like to pick Rock, Paper, or Scissors? ')
    player = player.lower()

    if player == computer:
        print('Computer also picked {}. It is a draw'.format(player))

    if player == 'rock':
        if computer == 'scissors':
            print('''You won. Computer picked scissors that were broken by
            your rock.''')
        if computer == 'paper':
            print('''Computer won. Computer picked paper that covered your
            rock.''')

    if player == 'scissors':
        if computer == 'paper':
            print('''You won. Computer picked paper that was cut by
            your scissors.''')
        if computer == 'rock':
            print('''Computer won. Computer picked rock that broke your
            scissors.''')

    if player == 'paper':
        if computer == 'rock':
            print('''You won. Computer picked rock that was covered by
            your paper.''')
        if computer == 'scissors':
            print('''Computer won. Computer picked scissors that cut
            your paper.''')
    


    