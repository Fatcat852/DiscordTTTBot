# base game code
# trying to adapt logic to discord bot
# -----Global Variables-----
game_still_going = True

# who won?
winner = None

#who's turn is it
player_1 = input("Please enter Player 1's name: ")
player_2 = input("Please enter Player 2's name: ")
current_player = player_1
symbol = "X"

# Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def start_game():
    global player_1, player_2
    want_to_play = False
    print("Hello " + player_1 + " and " + player_2 + "!")
    while not want_to_play:
        start = str(input("Would you like to play Tic Tac Toe?    ").lower())
        if start == "yes":
            want_to_play = True
        elif start == "no":
            print(":(")
    play_game()

def play_game():
    # Display initial board
    display_board()

    # Main game loop
    while game_still_going:

        #handle a turn
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #Flip to the other player
        flip_player()

    # Game ends
    who_is_winner()
    play_again()

def play_again():
    print("Wow! That was a great game!")
    want_to_play_again = False
    while not want_to_play_again:
        lets_play_again = str(input("Do you want to play again?    ").lower())
        if lets_play_again == "yes":
            want_to_play_again = True
        elif lets_play_again == "no":
            print("Aww... Okay... Goodbye!")
            exit()
    play_game()

#game checks
def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # global variables
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check_diagonals()
    diagonals_winner = check_diagonals()
    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonals_winner:
        winner = diagonals_winner

    else:
        winner = None

    return

def check_rows():
    # global variables
    global game_still_going
    #check if rows have the same value and are not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner (x or o)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

# check who the winner is
def who_is_winner():
    if winner == "X":
        print(player_1 + " won the game.")
    elif winner == "O":
        print(player_2 + " won the game.")
    elif winner == None:
        print("It was a tie.")

def check_columns():
    # global variables
    global game_still_going
    # check if rows have the same value and are not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (x or o)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    # global variables
    global game_still_going
    # check if rows have the same value and are not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner (x or o)
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

# Handle a single turn of an arbitrary player
def handle_turn(player):
    #global variables for this function
    global current_player
    print("It is " + current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position between 1 and 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Invalid input.")

    board[position] = symbol
    display_board()

def flip_player():
    global current_player, symbol
    if current_player == player_1:
        current_player = player_2
        symbol = "O"
    elif current_player == player_2:
        current_player = player_1
        symbol = "X"
    return
start_game()




