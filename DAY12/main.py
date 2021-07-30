def main():
    import random
    from art import logo
    """ use Global variable for number of turns """
    EASY = 10
    HARD = 5
    # create a guess game
    """ The program choose a number between 1 to 100 and want the user guess it """
    """ Remember user has limit chance to guess """

    """ a function for get the level of game and turns from user"""
    def ask():
        print("Welcome to the Number Guessing Game!"'\n'"I'm thinking about a number between 1 and 100")
        while True:
            dif = input("Choose a difficulty.Type 'easy' or 'hard' : ").lower()
            if dif == 'easy':
                time = EASY
                break
            elif dif == 'hard':
                time = HARD
                break
            else:
                print('WHAT ?!')

        return time

    """ Now we geting numbers from user in every turn and make sure its true or not """
    def get_guess(guess_time, choosen):
        y = 0 # y is a counter for show to the user how many turns remain
        for i in range(guess_time):
            print(F"You have {guess_time - y } attempts remaining to guess the number.")
            y += 1
            user_guess = int(input('make a guess: '))
            if user_guess == choosen:
                print(F"You got it.The number was {choosen}")
                break
            elif y == guess_time:
                print("You've ran out of guesses.You lose.")
            elif user_guess < choosen:
                print("Too low."'\n'"Guess again.")
            elif user_guess > choosen:
                print("Too high."'\n'"Guess again.")


    print (logo)
    choosen = random.randint(1, 101)#choose a random number between 1 and 100
    print(choosen)
    guess_time = ask()
    get_guess(guess_time, choosen)


main()
