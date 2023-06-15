from art import logo
import os
print(logo)

#HINT: You can call clear() to clear the output in the console.

bids={}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == 'no':
        bidding_finished = True
    elif more_bidders == 'yes':
        os.system('cls')

highest_bid = 0
for bid in bids:
    if bids[bid] > highest_bid:
        highest_bid = bids[bid]
        winner = bid
        
print(f"The winner is {winner} with a bid of ${highest_bid}.")
