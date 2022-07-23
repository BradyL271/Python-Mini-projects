import random

# Dafault values
player_choice = None
winner = "Tie"

# Turns player letter selection into the selected word.


def translator(choice):
    if choice == "R":
        return "Rock"
    elif choice == "P":
        return "Paper"
    elif choice == "S":
        return "Scissors"


# Determines the winner of the game.
def winner_calculator(player_selection, computer_selection):
    if player_selection == "Rock":
        if computer_selection == "Rock":
            return "Tie"
        elif computer_selection == "Paper":
            return "Computer wins"
        elif computer_selection == "Scissors":
            return "Player wins"
    elif player_selection == "Paper":
        if computer_selection == "Rock":
            return "Player wins"
        elif computer_selection == "Paper":
            return "Tie"
        elif computer_selection == "Scissors":
            return "Computer wins"
    elif player_selection == "Scissors":
        if computer_selection == "Rock":
            return "Computer wins"
        elif computer_selection == "Paper":
            return "Player wins"
        elif computer_selection == "Scissors":
            return "Tie"


# Game loop. Goes until one player wins.
while winner == "Tie":
    # Player makes selection
    print("\n\n\n\n\n\n\n\n\n\n\nChoose rock (r), paper (p), or scissors (s).")
    player_choice = input()
    player_choice = player_choice.upper()

    # Error handling for when the selection is not rock, paper, or scissors.
    while player_choice != "R" and player_choice != "P" and player_choice != "S":
        print("Invalid choice. Please choose again.")
        print("Choose rock (r), paper (p), or scissors (s).")
        player_choice = input()
        player_choice = player_choice.upper()

    # Turns player letter selection into the selected word.
    player_selection = translator(player_choice)

    # Computer Selection
    computer_choice_list = ["R", "P", "S"]
    computer_choice = computer_choice_list[random.randint(0, 2)]
    computer_selection = translator(computer_choice)

    # Player and computer printed results.
    print(f"You chose {player_selection}")
    print(f"The computer chose {computer_selection}")

    # Calculates winner.
    winner = winner_calculator(player_selection, computer_selection)
    print(winner_calculator(player_selection, computer_selection))
    if winner == "Tie":
        print("Play again.")
