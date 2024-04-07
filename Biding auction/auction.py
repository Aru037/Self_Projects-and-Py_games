from art import logo
print(logo)

bid = {}
bidding_finish = False

import os

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def highest_bidder(bidding_record):
    highest_bid = 0
    winner =""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finish:
    name =input("Enter your name: ")
    price =int(input("Enter your bid:$ ")) 
    bid[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finish = True
    elif should_continue == "yes":
        clear_screen()
    highest_bidder(bid)
    
