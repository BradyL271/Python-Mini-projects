# Creates the hangman.
def hangman(guessesleft):
    if guessesleft == 6:
        print("-------")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
    elif guessesleft == 5:
        print("-------")
        print("|     O")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
    elif guessesleft == 4:
        print("-------")
        print("|     O")
        print("|     |")
        print("|     |")
        print("|      ")
        print("|      ")
    elif guessesleft == 3:
        print("-------")
        print("|     O")
        print("|    /|")
        print("|   / |")
        print("|      ")
        print("|      ")
    elif guessesleft == 2:
        print("-------")
        print("|     O")
        print("|    /|\\")
        print("|   / | \\")
        print("|      ")
        print("|      ")
    elif guessesleft == 1:
        print("-------")
        print("|     O")
        print("|    /|\\")
        print("|   / | \\")
        print("|    / ")
        print("|   /  ")
    elif guessesleft == 0:
        print("-------")
        print("|     O")
        print("|    /|\\")
        print("|   / | \\")
        print("|    / \\")
        print("|   /   \\")

# verifys whether letter has already been chosen.


def check_if_letter_is_new(already_chosen_letters):
    new_letter = True
    print(already_chosen_letters)
    for letter in already_chosen_letters:
        if letter == letter_choice:
            new_letter = False
    return new_letter


# Player initial word setup.
word = input("Choose a word: ")
word = word.upper()

# Error handling if word has a space.
while " " in word:
    print("Must be one word.")
    word = input("Choose a word: ")

# Creates lines to display.
spaces = "_" * len(word)
spaces_list = list(spaces)

# Variable default values.
empty_space_counter = 1
guessesleft = 6
word_index = []
already_chosen_letters = []
incorrect_already_chosen_letters = []

# While loop for when player wins or loses.
while guessesleft > 0 and empty_space_counter > 0:

    # Player letter choice
    print(f"\n\n\n\n\n\n\n\n\n\n\n")
    {hangman(guessesleft)}
    print(f"\n{''.join(spaces_list)}")
    if len(incorrect_already_chosen_letters) > 0:
        print(
            f"Incorrect guesses: {', '.join(incorrect_already_chosen_letters)}")
    print(f"Guesses left: {guessesleft}")
    letter_choice = input("Choose a letter: ")

    # Error handling if more than 1 letter
    while len(letter_choice) != 1:
        print("\n\n\nMust select one letter")
        letter_choice = input("Choose a letter: ")

    # verifys whether letter has already been chosen, and adds chosen letter to list. Loops if letter has already been chosen,
    # and ends when a new letter has been chosen.
    new_letter = check_if_letter_is_new(already_chosen_letters)
    while new_letter == False:
        print(f"\n\n\n\n\n\n\n\n\n\n\n")
        {hangman(guessesleft)}
        print(f"\n{''.join(spaces_list)}")
        if len(incorrect_already_chosen_letters) > 0:
            print(
                f"Incorrect guesses: {', '.join(incorrect_already_chosen_letters)}")
        print(f"Guesses left: {guessesleft}")
        print("Letter has already been chosen")
        letter_choice = input("Choose a letter: ")
        new_letter = check_if_letter_is_new(already_chosen_letters)

    # Compares chosen letter to letters in word by looping through word. Adds new letter to list if incorrect.
    letter_in_word = False
    for letter in range(len(word)):
        if word[letter] == letter_choice.upper():
            word_index.append(letter)
            letter_in_word = True
            already_chosen_letters.append(letter_choice)
    if letter_in_word == False:
        incorrect_already_chosen_letters.append(letter_choice)

    # Subtracts guess amount if no letter in word.
    if letter_in_word == False:
        guessesleft -= 1

    # Updates the space list to display.
    for number in word_index:
        spaces_list[number] = word[number]

    # Checks to see how many spaces are left. If there are none, the player has won, and the while loop will end.
    empty_space_counter = 0
    for value in spaces_list:
        if value == "_":
            empty_space_counter += 1

# Determines whether the player won or lost.
if empty_space_counter <= 0:
    print(f"\n\n\n\n\n\n\n\n\n\n\n")
    hangman(guessesleft)
    print(f"\nThe word was \"{''.join(spaces_list)}\"")
    print("You win!")
else:
    print(f"\n\n\n\n\n\n\n\n\n\n\n")
    hangman(guessesleft)
    print("\nYou lose.")
    print(f"\nThe word was \"{word}\"")
