# A FUNCTION FOR CHECK LETTERS OF A WORD FOR HANGMAN

def check(w):
    # w is a word that ganna be randomly choose from a list
    # w = input('input your word :')

    man = [
        '''
        +---+
        |   |
            |
            |
            |
            |
        ========='''

        ,

        '''
        +---+
        |   |
        O   |
            |
            |
            |
        ========='''

        ,

        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        ========='''

        ,

        '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        '''
        ,
        '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        ========='''
        ,
        '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
    
        '''

        ,

        '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        ========='''
    ]

    # e is a list i creat to show for user how many letter our random word have
    e = []
    for i in range(len(w)):
        e.append("_")

    print(e)
    print()

    print(man[0])
    print()

    # t is my counter for letting user make guess(in this case 6 time)
    t = 1

    # now we let user guess and check the user's guess is right or not
    while (t <= 6):

        ap = 0  # ap is a counter
        # now we let user make guess for next letter
        g = input('what is your guess for words letters ? ')
        g = g.lower()
        # and now we check it
        for i in range(0, len(w)):
            if g == w[i]:
                e[i] = g
                ap += 1

        if ap == 0:
            print(f'erorr   {t}    :your guess is not right')
            print(man[t])
            t += 1

        if "_" not in e:
            print('the man stay alive')
            break

        elif "_" in e and t > 6:
            print("he is dead")

        print(e)
