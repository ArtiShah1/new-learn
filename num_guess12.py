import random

anemiess = 1
def increse_enemies():
    anemies = 2
    print(anemies)
print(anemiess)
increse_enemies()

player_health = 10
def healthy_player():
    football = 5
    print(player_health, "foot ball has", football)
print("this is value", anemiess)
healthy_player()
# game_level = 5
# all_games = ["skating", "tennis", "football", "cricket", "baseball"]
# if game_level < 2:
#     new_game = all_games[1]
# print(new_game)


# --------------------no gussing game -------------------
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("you are too high")
        return turns - 1
    elif guess < answer:
        print("you are low")
        return turns - 1
    else:
        print(f"you are right!{answer}")
# make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # choosing a random number between 1 and 100.
    print("welcome to the number guessing game")
    print("i am thinking of a number between 1 and 100")
    answer = random.randint(1,100)
    print(f"pssst, the correct answer is {answer}")
    turns = set_difficulty()

    # repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess"))
        turns = check_answer(guess,answer, turns)
        if turns == 0:
            print("you've run out of guesses, you lose.")
            return

game()






