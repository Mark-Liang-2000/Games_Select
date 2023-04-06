import random

# Define the options
options = ["r", "p", "s"]

# Define a function to get the user's choice
def get_user_choice():
    user_choice = input("Choose r, p, or s: ").lower()
    while user_choice not in options:
        user_choice = input("Invalid choice. Choose r, p, or s: ").lower()
    return user_choice

# Define a function to get the computer's choice
def get_computer_choice():
    return random.choice(options)

# Define a function to determine the winner
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Tie"
    elif (choice1 == "r" and choice2 == "s") or (choice1 == "p" and choice2 == "r") or (choice1 == "s" and choice2 == "p"):
        return str(choice1) + " wins!"
    else:
        return str(choice2) + " wins!"

# Define a function to keep track of the score
def keep_score(player1_score, player2_score, result):
    if result == "Tie":
        pass
    elif "wins!" in result:
        if result[0] == "r":
            player1_score += 1
        else:
            player2_score += 1
    print("Score: Player 1 -", player1_score, "Player 2 -", player2_score)
    return player1_score, player2_score


def play_rps():
    # Initialize the scores
    player1_score = 0
    player2_score = 0

    # Open a file to log the game results
    with open("game_results.txt", "a") as f:
        f.write("Rock Paper Scissor's Session Results\n")

    # Play the game
    print("Let's play Rock Paper Scissors!")
    opponent = str(input("Do you want to play against the computer? (y/n)"))

    while opponent.lower() != "y" and opponent.lower() != "n":
        opponent = str(
            input("Invalid choice. Do you want to play against the computer? (y/n)"))

    while True:
        if opponent.lower() == "y":
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print("You chose", user_choice)
            print("The computer chose", computer_choice)
            result = determine_winner(user_choice, computer_choice)
            print(result)
            player1_score, player2_score = keep_score(
                player1_score, player2_score, result)

            # Write the game result to the file
            with open("game_results.txt", "a") as f:
                f.write(
                    f"You: {user_choice}, Opponent: {computer_choice}, Result: {result}\n")

        elif opponent.lower() == "n":
            user_choice1 = get_user_choice()
            user_choice2 = get_user_choice()
            print("Player 1 chose", user_choice1)
            print("Player 2 chose", user_choice2)
            result = determine_winner(user_choice1, user_choice2)
            print(result)
            player1_score, player2_score = keep_score(
                player1_score, player2_score, result)

            # Write the game result to the file
            with open("game_results.txt", "a") as f:
                f.write(
                    f"Player 1: {user_choice1}, Player 2: {user_choice2}, Result: {result}\n")

        while True:
            # First break out of this try/expect loop
            try:
                play_again = input("Do you want to play again? (y/n)")
                if play_again.lower() == "n":
                    break
                elif play_again.lower() != "y":
                    raise ValueError(
                        "Invalid choice. Please choose 'y' or 'n'.")
            except ValueError as e:
                print(e)
                continue
            break

        # Second break out of master try/expect loop
        if play_again.lower() == "n":
            break

    print("Final Score: You: ", player1_score, "Opponent: ", player2_score)


# play_rps()
