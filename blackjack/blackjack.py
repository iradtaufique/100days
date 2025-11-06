import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# creating a function that return random card
def deal_card(card):
    random_card = card[random.choice(card)]
    return random_card

# assigning 2 random cards for user and computer
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))

