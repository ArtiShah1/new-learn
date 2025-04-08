import random

word_list =("ardvark", "baboon", "camel")

# TODO 1 - Rendomly chose a word from the word_list and assign it to a variable called  chosen_word.

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing Code
print(f"Pssst, the solution is {chosen_word}")
display = []

for letter in range(word_length):
    display += "_"

# TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess.make guess lowercase.


# TODO 3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.

end_of_game = False
while not end_of_game:
    guess = input("Gess a letter :").lower()
    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"current posigtion: {position}/n current letter: {letter}/n guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
if guess not in chosen_word:
    lives = 1
    if lives == 0:
        end_of_game = True
        print("you lose")

print(display)
print(f"{''.join(display)}")
if "_" not in display:
    end_of_game = True
    print("you Win")







