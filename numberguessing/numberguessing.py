import logo
import random

hidden_number = random.randint(1,100)
print(hidden_number)


print(logo.logo)

print('Welcome to the Number Guessing Game')
print('I am Thinking a number between 1 and 100')
game_level = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()

def easy_level(level):
    if level == 'easy':
        attempt = 10
    else:
        attempt = 5
    found_number = False
    end_game = False
    while not found_number and not end_game:
        print(f"you Have {attempt} Attempt remaining to guess the number")
        guess = int(input("Make a guess:  "))
        if guess == hidden_number:
            print(f"You got it the number was {guess}")
            found_number = True

        else:
            attempt -= 1
            if attempt == 0:
                end_game = True
            if guess > hidden_number:
                print(f"Too High ")
            else:
                print(f"Too Low")


if game_level == 'easy':
    easy_level(game_level)
elif game_level == 'hard':
    easy_level(game_level)
else:
    print('Invalid Game Level, Choose easy or Hard')
