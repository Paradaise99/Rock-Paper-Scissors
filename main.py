from random import randint 

game = ['Rock', 'Paper', 'Scissors']

computer = game[randint(0,2)]

player = False 

while player == False:
    player = input('Rock, Paper, Scissors?')
    if player == computer:
        print('That was a Tie')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You Lose!', computer, 'covers', player)
        else:
            print('You Win!', player, 'smashes', computer)

    elif player == 'Paper':
        if computer == 'Scissors':
            print('You Lose!', computer, 'cuts', player)
        else:
            print('You Win!', Player, 'covers', computer)

    elif player == 'Scissors':
        if computer == 'Rock':
            print('You Lose!', computer, 'smashes', player)
        else:
            print('You Win!', Player, 'cuts', computer)

    else:
        print('That is an invalid input')

player = False

computer = game[randint(0/2)]






