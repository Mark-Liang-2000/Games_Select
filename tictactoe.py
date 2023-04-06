board = {1: ' ',  2: ' ',  3: ' ',
         4: ' ',  5: ' ',  6: ' ',
         7: ' ',  8: ' ',  9: ' '}

# Making the board appear


def render():
    board_state = f'''
{board[1]}|{board[2]}|{board[3]}
-+-+-
{board[4]}|{board[5]}|{board[6]}
-+-+-
{board[7]}|{board[8]}|{board[9]}
'''
    return board_state

# Asking player to make a move


def get_action(player):
    while True:
        try:
            action = int(input(f"Player {player}, choose a spot: "))
            if action < 1 or action > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if board[action] != ' ':
                print("Spot already taken. Please choose another spot.")
                continue
            return action
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# You win


def victory_message(player):
    print(render())
    return f"Player {player} wins!"

# All possible solutions to t3


def check_win(player):
    win_conditions = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Playing the game


def play_t3():
    player = 'X'
    game_round = 0
    game_over = False

    while not game_over:
        print(render())
        action = get_action(player)
        board[action] = player
        game_round += 1
        if game_round >= 4:
            if check_win(player):
                print(victory_message(player))
                with open('games_results.txt', 'a') as file:
                    file.write(f"{player} won the game!\n")
                game_over = True
                break
        if game_round == 9:
            print(render())
            print("Tie game!")
            with open('games_results.txt', 'a') as file:
                file.write("Tie game!\n")
            game_over = True
            break

        # Deciding the player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    # Reseting the board to a clean state
    restart = input("Play again? (y/n)").lower()
    if restart == 'y':
        for key in board:
            board[key] = ' '
        play_t3()


play_t3()
