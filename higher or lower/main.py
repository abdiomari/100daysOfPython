from turtle import clear
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """# format the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return(f"{account_name}, a {account_description}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """take the user guess and follower counts and return if they are right"""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

# display art 
print(logo)
score = 0 
game_should_continue = True
account_b = random.choice(data)

# make game repeatable
while game_should_continue:

    # generate a random account from the game data 
    # making the accounts at position B become the next account at position A
    account_a = account_b  
    account_b = random.choice(data)

    while account_a == account_b :
        account_b =  random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")



    # ask the  user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' : \n").upper()
    # check if user is correct

        # get folllower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
        # use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
# clear screen between rounds
    clear
    # give user feedback on their guess
     # keep score
    score = 0
    if is_correct:
        score += 1
        print(f"you are right, Current score{score}")
    else:
        print(f"Sorry that is wrong, you got {score}")
       
   

