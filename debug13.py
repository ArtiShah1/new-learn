# Debugging
# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print(i)
#             print("you got it")
# my_function()
# # ----------while------
# i = 1
# while i <21:
#     if i ==20:
#      break
#     else:
#         print(i)
#     i +=1
#  -------------reproduce the bug-----------
# from random import randint
# dice_image = ["1","2","3","4","5","6"]
# dice_num = randint(0,5)
# print(dice_image[dice_num])

# -------Play Computer ----------------
# year = int(input("what is your year of birth"))
# if year >= 1980 and year <= 1994:
#     print("you are millennial")
# elif year > 1994:
#     print("you are a Gen Z")
#
# pages = 0
# word_per_page = 0
# pages = int(input("number of pages"))
# word_per_page == int(input("Number of words per page"))
# total_words = pages * word_per_page
# print(total_words)

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
# mutate([1,2,3,4,5,9,13])

# number = int(input("what is your number to check or ir even?"))
#
# if number % 2 == 0:
#     print("this number is even")
# else:
#     print("this number is odd")

# year = int(input("which year do you want to check?"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#              print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")
#
# target = int(input("your number"))
# for number in range(1, target+1):
#     if number % 3 == 0 and  number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# ...........High to Low............
from game_data import data
import random
import clear

def get_random_account():
    """Get data from random account"""
    return random.choice(data)



#  format the account data into printable format
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a{account_descr}, from {account_country}"

def check_aswer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print("Higher & Lower game")
    score = 0
    game_should_continue = True

#  generate random account from data
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"compare A: {format_data(account_a)}")
        print("Vs")
        print(f"compare B: {format_data(account_b)}")

# Take the user guess and follower counts and returns if they got it right"""
# ask user for a guess.
        guess = (input("who has more follower? A or B").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
        print(f"You're right! Current score: {score}.")
        else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

game()
        # check if user is correct.
# Get follower count of each account
# give user feedback on their guess



