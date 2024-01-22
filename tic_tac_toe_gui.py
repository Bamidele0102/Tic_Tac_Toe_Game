import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import display_board, player_input, place_marker, win_check, choose_first, space_check, full_board_check

app = tk.Tk()
app.title('Tic Tac Toe')

buttons = [None] + [tk.Button(app, text=' ', font=('Helvetica', 24), width=4, height=2) for _ in range(9)]

def clear_board():
    """
    Clears the Tic Tac Toe board, resets game state, and displays the new board.
    """
    global theBoard, player1_marker, player2_marker, turn
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    display_board()

def on_click(position):
    """
    Handles button click events on the Tic Tac Toe board.

    Parameters:
    - position (int): The position (1-9) on the board where the player clicked.
    """
    global turn
    if space_check(theBoard, position):
        if turn == 'Player 1':
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker, position):
                display_board()
                messagebox.showinfo('Game Over', 'Congratulations! Player 1 has won!')
                clear_board()
            else:
                turn = 'Player 2'
        else:
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker, position):
                display_board()
                messagebox.showinfo('Game Over', 'Congratulations! Player 2 has won!')
                clear_board()
            else:
                turn = 'Player 1'
        display_board()

app = tk.Tk()
app.title('Tic Tac Toe')

buttons = [None] + [tk.Button(app, text=' ', font=('Helvetica', 24), width=4, height=2, command=lambda pos=pos: on_click(pos)) for pos in range(1, 10)]

def display_board():
    """
    Updates the GUI to reflect the current state of the Tic Tac Toe board.
    """
    for pos, button in enumerate(buttons[1:], start=1):
        button['text'] = theBoard[pos]

for row in range(3):
    for col in range(3):
        buttons[row * 3 + col + 1].grid(row=row, column=col)

clear_button = tk.Button(app, text='Clear Board', command=clear_board)
clear_button.grid(row=3, column=0, columnspan=3)

app.mainloop()
