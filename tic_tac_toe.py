import os
""" This is a module that contains functions that will be used in the main program. """
import random
""" Writing a function that will randomly choose a position for the player to place their marker. """

def clear_output():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board, current_turn):
    """
    Displays the Tic Tac Toe board.

    Parameters:
    - board (list): The current state of the board.
    - current_turn (str): The current player's turn ('Player 1' or 'Player 2').
    """
    clear_output()
    print(f"\n{current_turn}'s turn:")
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('---|---|---')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('   |   |   ')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board, 'Player 1')

def player_input():
    """ Asks the player if they want to be X or O. """
    marker = ''

    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?\n').upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

def place_marker(board, marker, position):
    """
    Takes in a board list object, a marker ('X' or 'O'),
    and a desired position (number 1-9) and assigns it to the board.
    """
    board[position] = marker

def win_check(board, mark):
    """ Takes in a board and checks if a player won. """
    return (
        (board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark) # diagonal
    )

def choose_first():
    """ Randomly choose the player who goes first. """
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    """ Checks if a space on the board is free. """
    return board[position] == ' '

def full_board_check(board):
    """ Checks if the board is full. """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    """Asks for a player's next position (1-9) and return the position."""
    while True:
        try:
            position = int(input('Choose your next position: (1-9) '))
            if position in range(1, 10) and space_check(board, position):
                return position
            else:
                print('Invalid input. Please choose a number between 1 and 9.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

def replay():
    """ Asks the player if they want to play again. """
    response = input('Do you want to play again? Enter Yes or No: ').lower()
    return response == ('yes')

print('Welcome to Tic Tac Toe Game!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No\n')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard, turn)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard, turn)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                turn = 'Player 2'

        else:
            # Players2's turn.

            display_board(theBoard, turn)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard, turn)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard, turn)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'
        
        if not replay():
            break
