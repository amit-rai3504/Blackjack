############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random 
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's draw")
    elif user_score == 0:
        print("You Win as you got Blackjack")
    elif computer_score == 0:
        print("You lose as dealer got Blackjack")
    elif user_score > 21:
        print(f"You lose as your score reached greater than 21, Dealer's score : {computer_score}")
    elif computer_score > 21:
        print(f"You win as dealer's score reached greater than 21, your score : {user_score}")
    elif computer_score > user_score:
        print(f"You lose as dealer got more score,  your score : {user_score} and Dealer's Score : {computer_score}")
    else:
        print(f"You Win as you got more score, your score : {user_score} and Dealer's Score : {computer_score}")

def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    game_ends = False
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    print(f"your cards : {user_cards}")
    computer_card_to_show = random.choice(computer_cards)
    print(f"Dealer's first card: {computer_card_to_show}")
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    while not game_ends:
        if user_score == 0:
            print("You Win as you got Blackjack")
            game_ends = True
        elif computer_score == 0:
            print("You lose as computer got Blackjack")
            game_ends = True
        elif user_score > 21:
            print("You lose as your score reached greater than 21")
            game_ends = True
        
        new_card = input("Do you want to draw new card press yes or no :").lower()
        
        while new_card == "yes":
            user_cards.append(random.choice(cards))
            user_score = calculate_score(user_cards)
            print(f"your cards : {user_cards}")
            new_card = input("Do you want to draw new card press yes or no :").lower()
            
        while computer_score < 17 and computer_score!=0:
            computer_cards.append(random.choice(cards))
            computer_score = calculate_score(computer_cards)
    
        compare(user_score, computer_score)
        new_game = input("do you want to restart the game. Yes or No :").lower()
        if new_game == "yes":
            blackjack()
        else:
            game_ends = True


blackjack()
