# black jack game project
# TODO 
# 1. create a deal_card() function to return a random card
import random
from turtle import clear
from art import logo


def deal_card():
    """returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

# 3. create a function called calculate_score() to take list of cards as input and returns the score as a sum
def calculate_score(cards): 
    """takes a list of cards and returns the score calculated """
    # 4. inside calculate_score() check for an ace. if the score is over 21 remove the 11 and replace it with a 1.
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
         
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)  

#9: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Backjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(logo)
    # 2. deal user and computer 2 cards each hint use deal_card funcion and append() method
    user_cards = []
    computer_cards = []

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(deal_card)

        

    # 5. call calculate score() if the computer or the user has a blackjack(0) or if the user's score is over 21 then game ends
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f" your cards:  {user_cards}, current score: {user_score}")
    print(f" your cards:  {computer_cards}, current score: {computer_score}")

    # 6. if not over ask the user if they want to draw another card if yes implement the deal card function to add another card if no the game is over

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'Y' to get another card, type 'N' to pass: ")
        if user_should_deal == "Y":
            user_cards.append(deal_card())
        else:
            is_game_over = True


    # 7: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    #8: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" your final hand:{user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final_score: {computer_score}")

    print(compare(user_score, computer_score))
    
#10: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' :  ") == "y":
    clear
    play_game()
