import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# creating a function that return random card
def deal_card(card):
    random_card = card[random.choice(card)]
    return random_card

deal_card(cards)

print(deal_card(cards))