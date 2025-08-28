import tkinter as tk
from board import XO_points, X_points, O_points, XOPoint
from logic import check_win, disable_game, winning_possibilities
from ai import auto_play

def setup_ui(root):
    global status_label, play_again_button, play_with_button, current_chr, play_with

    tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()
    status_label = tk.Label(root, text="X's turn", font=('Ariel', 15), bg='green', fg='snow')
    status_label.pack(fill=tk.X)

    play_again_button = tk.Button(root, text='Play again', font=('Ariel', 15), command=play_again)

    play_with_button = tk.Button(root, text='Play with human', font=('Ariel', 15), command=play_with_human)
    play_with_button.pack()

    play_area = tk.Frame(root, width=300, height=300, bg='white')
    play_area.pack(pady=10, padx=10)

    # Initialize the board
    for x in range(1, 4):
        for y in range(1, 4):
            XO_points.append(XOPoint(x, y, play_area, status_label, auto_play, check_win))

    # Defaults
    current_chr = "X"
    play_with = "Computer"

def play_again():
    global current_chr
    current_chr = 'X'
    for point in XO_points:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_label.configure(text="X's turn")
    play_again_button.pack_forget()

def play_with_human():
    global play_with
    play_with = "Human"
    play_with_button['text'] = "Play with computer"
    play_with_button['command'] = play_with_computer
    play_again()

def play_with_computer():
    global play_with
    play_with = "Computer"
    play_with_button['text'] = "Play with human"
    play_with_button['command'] = play_with_human
    play_again()
