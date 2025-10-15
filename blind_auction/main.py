import logo

# print the logo
print(logo.logo)

# declare an empty dictionary to store all the bidders value
all_bidders = {}


# Created a function that help to loop in all dictionary and get the highest amount
def max_bid_amount(bidders):
    high_bidder_value = 0
    bidder_name = ''
    for bid in bidders:
        max_bidder = bidders[bid]
        if max_bidder > high_bidder_value:
            high_bidder_value = max_bidder
            bidder_name = bid
    print(f'The winner of the auction is {bidder_name} with the highest bid amount of {high_bidder_value}')

# create a while loop that will help to get all bidders values
new_bidder_value = True
while new_bidder_value:
    # get user inputs, names and bid amount
    user_name = input('Enter your Name: ')
    bid_amount = int(input('Enter Bid Amount: $'))

    # Store the Bidders values in the dictionary
    all_bidders[user_name] = bid_amount

    # Ask if there is any other bidder
    next_bidder = input("Is there any other bidder? if there is Type Yes otherwise No ")

    if next_bidder.lower() == 'yes':
        #create a space for the second value
        print('\n' * 30)
    else:
        # if no other bidder loop from the dictionary and get bidder with high amount
        new_bidder_value = False
        max_bid_amount(all_bidders)




