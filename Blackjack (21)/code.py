import random
from art import logo

def deal_card():
    """Returns a random card from the deck."""

    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns added score in the list."""
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards) 

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "It's a Draw."
    elif computer_score == 0:
        return "You Lose, opponent had a blackjack!!!"
    elif user_score == 0:
        return "You Win with a blackjack!!!"
    elif user_score > 21:
        return "You went over. You Lose."
    elif computer_score > 21:
        return "Opponent went over. You Win."
    elif user_score > computer_score:
        return "You Win."
    else:
        return "You Lose."

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your current cards are {user_cards}, and the score is {user_score}.")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Enter 'y' to draw one card or 'n' to pass: ")
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards) 


    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

    while input("Do you want to play another Game? Type 'y' or 'n': ") == "y":
        play_game()

play_game() 