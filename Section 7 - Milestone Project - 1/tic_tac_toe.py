'''
We need to print a board.
Take in player input.
Place their input on the board.
Check if the game is won,tied, lost, or ongoing.
Repeat c and d until the game has been won or tied.
Ask if players want to play again.
'''

game_on = True
play_again = False
board = ['','','','','','','','','']

print("Welcome to Tic Tac Toe Game!")

def display_board(board):
    print(board[6]+' | '+board[7]+' | '+board[8])
    print(board[3]+' | '+board[4]+' | '+board[5])
    print(board[0]+' | '+board[1]+' | '+board[2])

def player1_input():

    # VARIABLES
    num = ''
    within_range = False

    # CONDITIONS TO CHECK
    # DIGIT OR WITHIN_RANGE = FALSE
    while within_range == False or num.isdigit() == False:
        num = input("Player 1 [X] \t Pick a number between 1 and 9: ")

    # DIGIT CHECK
        if num.isdigit() == False:
            print("Not a number!")

    # RANGE CHECK
        if num.isdigit():
            if int(num) not in [1,2,3,4,5,6,7,8,9]:
                within_range = False
                print("You must add a number between 1 and 9")
            else:
                within_range = True
    return int(num)

def player2_input():

    # VARIABLES
    num = ''
    within_range = False

    # CONDITIONS TO CHECK
    # DIGIT OR WITHIN_RANGE = FALSE
    while within_range == False or num.isdigit() == False:
        num = input("Player 2 [Y] \t Pick a number between 1 and 9: ")

    # DIGIT CHECK
        if num.isdigit() == False:
            print("Not a number!")
            
    # RANGE CHECK
        if num.isdigit():
            if int(num) not in [1,2,3,4,5,6,7,8,9]:
                within_range = False
                print("You must add a number between 1 and 9")
            else:
                within_range = True
    return int(num)

def make_player1_input_appear_on_board(player1_input, board):
    place = player1_input()

    if board[place-1] == '':
        board[place-1] = 'X'
    else:
        print("You cannot place your mark there")

    return board

def make_player2_input_appear_on_board(player2_input, board):
    place = player2_input()

    if board[place-1] == '':
        board[place-1] = 'O'
    else:
        print("You cannot place your mark there")

    return board

def check_game_status(board):

    winner = False

    # ROW X
    if board[0] == board[1] == board[2] == 'X':
        winner = True
        print("Player1 won")
    elif board[3] == board[4] == board[5] == 'X':
        winner = True
        print("Player1 won")
    elif board[6] == board[7] == board[8] == 'X':
        winner = True
        print("Player1 won")
    # ROW Y
    if board[0] == board[1] == board[2] == 'Y':
        winner = True
        print("Player1 won")
    elif board[3] == board[4] == board[5] == 'Y':
        winner = True
        print("Player1 won")
    elif board[6] == board[7] == board[8] == 'Y':
        winner = True
        print("Player1 won")
    # COLUMN X
    if board[0] == board[3] == board[6] == 'X':
        winner = True
        print("Player1 won")
    elif board[1] == board[4] == board[7] == 'X':
        winner = True
        print("Player1 won")
    elif board[2] == board[5] == board[8] == 'X':
        winner = True
        print("Player1 won")
     # COLUMN Y
    if board[0] == board[3] == board[6] == 'Y':
        winner = True
        print("Player1 won")
    elif board[1] == board[4] == board[7] == 'Y':
        winner = True
        print("Player1 won")
    elif board[2] == board[5] == board[8] == 'Y':
        winner = True
        print("Player1 won")
    
    if winner == False:
        print("\nContragulations!")
        return True
        
    else:
        return False


while game_on:
    display_board(board)
    make_player1_input_appear_on_board(player1_input, board)
    display_board(board)
    game_on = check_game_status(board)
    make_player2_input_appear_on_board(player2_input, board)
    display_board(board)
    game_on = check_game_status(board)



