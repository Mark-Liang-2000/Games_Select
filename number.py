import random

# Random target number


def generate_random_number():
    return random.randint(1, 100)

# How close the game is to the target number


def check_guess(guess, target):
    if guess == target:
        print("You guessed it!")
        return True
    elif abs(guess - target) <= 5:
        print("Hot")
        return False
    elif abs(guess - target) <= 10:
        print("Warm")
        return False
    else:
        print("Cold")
        return False


def play_number():
    target_number = generate_random_number()
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    num_guesses = 0
    while True:
        num_guesses += 1
        try:
            guess = input("Enter your guess (or 'q' to quit): ")
            if guess == "q":
                print("The number was", target_number, "Thanks for playing!")
                with open("game_results.txt", "a") as file:
                    file.write(
                        f"Number Guessing Game Results--- Target Number: {target_number}, Tries: {num_guesses}\n")
                return
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        correct = check_guess(guess, target_number)
        if correct:
            print("You guessed the number in", num_guesses,
                  "guesses! Thanks for playing!")
            with open("game_results.txt", "a") as file:
                file.write(
                    f"Target Number: {target_number}, Tries: {num_guesses}\n")
            break

    while True:
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == "y":
            play_number()
            break
        elif play_again == "n":
            print("Thanks for playing!")
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


# play_number()
