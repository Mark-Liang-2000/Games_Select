import tictactoe
import rps
import number


def tic_tac_toe():
    print("Playing Tic-Tac-Toe!")
    tictactoe.play_t3()


def rock_paper_scissors():
    print("Playing Rock Paper Scissors!")
    rps.play_rps()


def number_guessing_game():
    print("Playing Number Guessing Game!")
    number.play_number()


while True:
    print("Please select a game to play:")
    print("1. Tic-Tac-Toe")
    print("2. Rcok Paper Scissors")
    print("3. Number Guessing Game")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 4:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        tic_tac_toe()

    elif choice == 2:
        rock_paper_scissors()

    elif choice == 3:
        number_guessing_game()

    elif choice == 4:
        print("Thanks for playing!")
        break
