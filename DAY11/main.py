from cleaner import clear
from art import logo
def main():

    import random

    def deal_card():
        """Return a random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)

        return card

    def calculate_sccore(card_list):#for calculate scores

        if sum(card_list) == 21 and len(card_list) == 2:
            return 0
        elif sum(card_list) > 21 and 11 in card_list:
            """1 and 11 are ace and we can choose which is better for deck"""
            card_list.remove(11)
            card_list.append(1)
        return sum(card_list)

    def compare(user_card, system_card):#this function say who is winner
        user_score = calculate_sccore(user_card)
        system_score = calculate_sccore(system_card)

        if system_score == user_score:
            print('draw.')
        elif system_score == 0:
            print('system has blackjack.you lose')
        elif user_score == 0:
            print("win with a blackjack")
        elif system_score > 21:
            print(F"system cards are: {system_card},system score is: {system_score}")
            print('system busted.you win.')
        elif user_score > 21:
            print(F"your cards are: {user_card},your score is: {user_score}")
            print('you busted.you lose.')
        elif user_score < system_score and user_score != 0:
            print(F"system cards are: {system_card},system score is: {system_score}")
            print(F"your cards are: {user_card},your score is: {user_score}")
            print('you lose.')
        elif user_score > system_score and system_score != 0:
            print(F"system cards are: {system_card},system score is: {system_score}")
            print(F"your cards are: {user_card},your score is: {user_score}")
            print('you win.')

    user_card = []
    system_card = []
    is_game_over = False

    for i in (user_card, system_card):#choosing cadrs for every deck
        i.append(deal_card())
        i.append(deal_card())

    while not is_game_over:
        user_score = calculate_sccore(user_card)
        system_score = calculate_sccore(system_card)
        print(F"    the user cards is: {user_card} and user score is: {user_score}")
        print(F"    the system first card is: {system_card[0]}")

        if user_score == 0 or system_score == 0 or user_score > 21:
            is_game_over = True
        else:
            add = input("do you wanna add another card? (yes/no) ").lower()
            if add == "yes":
                user_card.append(deal_card())

            else:
                is_game_over = True

    while system_score != 0 and system_score < 17:
        system_card.append(deal_card())
        system_score = calculate_sccore(system_card)

    compare(user_card, system_card)


play = True
while play:
    t = input("do you wanna play blackjack ? (yes/no) ").lower()
    if t != "yes":
        break
    print(logo)
    main()
    clear()
