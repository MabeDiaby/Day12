import random
from art import logo

print(logo)

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, number, turns):
    """Checks number aganist guess returns number of turns remaining"""
    if user_guess > number:
        print("Too High.")
        return turns -1
    elif user_guess < number:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it! The answer was {number}")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 101)
    print(number)
    turns = set_difficulty()

    user_guess = 0
    while user_guess != number:
        print(f"You have {turns} attempts remaing to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != number:
            print("Guess again.")
game()