# THIS IS A TIC TAC TOE GAME

import os
from time import sleep


# STEP 1: DISPLAY A BOARD

def display_board(board):
    # THIS FUNCTION WILL CREATE THE BOARD AND ALSO ERASE THE PREVIOUS BOARD

    sleep(0.2)

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print('     |     |     ')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + '  ')
    print('     |     |     ')
    print('——————————————————')
    print('     |     |     ')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + '  ')
    print('     |     |     ')
    print('——————————————————')
    print('     |     |     ')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + '  ')
    print('     |     |     ')


# STEP 2: ASSIGN MARKERS TO PLAYERS

def assign_marker():
    # THIS FUNCTION ASSIGNS MARKER TO PLAYERS AND RETURNS A TUPLE (P1,P2)

    p1 = ''
    while p1 not in ['X', 'O']:
        p1 = input('Please pick a marker "X" or "O": ').upper()
        if p1 not in ['X', 'O']:
            print("Invalid choice of markers, please choose either 'X' or 'O'")
    print("Player 1 : ", p1)
    if p1 == 'X':
        p2 = "O"
    else:
        p2 = "X"
    print("Player 2 : ", p2)
    return [p1, p2]


# STEP 3: CHOOSE TURN
def choose_first():
    # THIS FUNCTION WILL RANDOMLY DECIDE WHO WILL GO FIRST
    import random
    if random.randint(0, 1) == 0:
        print('Player 1 will go first')
        return 'p1'
    else:
        print('Player 2 will go first')
        return 'p2'


# STEP 4: CHECK BOARD FOR EMPTY SPACES
def check_board(board, pos):
    # THIS FUNCTION WILL CHECK ANY EMPTY SPACES IN THE BOARD
    return board[pos] == 'X' or board[pos] == 'O'


# STEP 5: DEFINE A MARKER POSITION
def position():
    """
    THIS FUNCTION DOES NOT ALLOW THE USER TO MARK ON AN ALREADY MARKED POSITION AND ENSURES THAT THE USER
    GIVES A VALID POSITION FORM 1 TO 9
    """
    pos = 0
    while pos not in [str(i) for i in range(1,10)] or check_board(board, int(pos)) == True:
        pos = input(turn + ": Where would you like to place your marker? ")
        if pos not in [str(i) for i in range(10)]:
            print('Please pick a number between 1 and 9')
            continue
        if board[int(pos)] == 'X' or board[int(pos)] == 'O':
            print('This place has already been marked. Please select another position')
    return int(pos)


# STEP 6: MODIFY THE BOARD
def mod_board(board, pos, marker):
    board[pos] = marker


# STEP 7: WIN CHECKER
def win_check(board):
    if ((board[7] == board[8] == board[9]) or (board[4] == board[5] == board[6]) or (
            board[1] == board[2] == board[3]) or
            (board[7] == board[4] == board[1]) or (board[8] == board[5] == board[2]) or (
                    board[9] == board[6] == board[3]) or
            (board[7] == board[5] == board[3]) or (board[1] == board[5] == board[9])):
        return True


# STEP 8: TIE CHECKER
def tie_check(board):
    for i in range(10):
        if board[i] not in ['X', 'O']:  # != 'X' or board[i] != 'O':
            return False
    return True


# STEP 9: ASK FOR A REPLAY
def replay():
    r = ' '
    while r[0] not in ['Y', 'N']:
        r = input('Do you wish to replay?\nYes or No: ').upper()
    return r.startswith('Y')


def play_game():
    g = ' '
    while g[0] not in ['Y', 'N']:
        g = input('Do you wish to start the game?\nYes or No: ').upper()
    return g.startswith('Y')


if __name__ == '__main__':
    while True:
        print('THIS IS A TIC TAC TOE GAME')
        board = [str(i) for i in range(10)]
        print(board)
        display_board(board)
        (p1, p2) = assign_marker()
        turn = choose_first()
        if play_game():
            game_on = True
        while game_on:
            if turn == 'p1':
                display_board(board)
                pos = position()
                mod_board(board, pos, p1)
                if win_check(board):
                    print('Congratulations! Player 1 won this game')
                    display_board(board)
                    game_on = False
                elif tie_check(board):
                    print('The game is drawn')
                    display_board(board)
                    game_on = False
                turn = 'p2'
            else:
                display_board(board)
                pos = position()
                mod_board(board, pos, p2)
                if win_check(board):
                    print('Congratulations! Player 2 won this game')
                    display_board(board)
                    game_on = False
                elif tie_check(board):
                    print('The game is drawn')
                    display_board(board)
                    game_on = False
                turn = 'p1'
        if not replay():
            break

