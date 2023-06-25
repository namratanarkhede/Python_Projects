logo = ('                              _   _            _   _                 _               \n'
        '                             | | | |          | \ | |               | |              \n'
        '   __ _ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ \n'
        '  / _` | | | |/ _ \/ __/ __| | __| \'_ \ / _ \ | . ` | | | | \'_ ` _ \| \'_ \ / _ \ \'__|\n'
        ' | (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   \n'
        '  \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   \n'
        '   __/ |                                                                             \n'
        '  |___/                                                                              ')

print(logo)
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

#function to check user's guess against actual answer
def check_answer(guess, answer , turns):
    if guess > answer:
        print("too high.")
        return turns - 1
    elif guess < answer:
        print("too low.")
        return turns - 1
    else:
        print(f"You got it! the answer was {answer}.")

#make function to set difficulty
def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
       return EASY_LEVEL_TURNS
    else:
       return HARD_LEVEL_TURNS

def game():
    #choosing a random no between 1 and 100
    print("Welcome to number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)

    turns = set_difficulty()

    # repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        #let the user guess the number
        guess = int(input("Make a guess :"))
        # track the number of turns and reduce by 1 if they are wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses, you lose")
            return
        elif guess != answer:
            print("guess again")


game()
