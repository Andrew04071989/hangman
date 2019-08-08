# import random
# words = []


def hangman(word):
    wrong = 0
    stages = ['',
              '__________          ',
              '|         |         ',
              '|         |         ',
              '|         O         ',
              '|        /|\        ',
              '|        / \        ',
              '|                   '
             ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to the execution!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Please, input char: '
        char = input(msg)
        if char in rletters:
            c_ind = rletters.index(char)
            board[c_ind] = char
            rletters[c_ind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You win! Word is: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! Word is: {}'.format(word))


# hangman(random.choice(words))
hangman(input('Первый игрок загадывает слово: '))

