import tkinter as tk

XO_points = []
X_points = []
O_points = []
current_chr = "X"
play_with = "Computer"

class XOPoint:
    def __init__(self, x, y, play_area, status_label, auto_play, check_win):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

        self.status_label = status_label
        self.auto_play = auto_play
        self.check_win = check_win

    def set(self):
        global current_chr, play_with
        if not self.value:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr
            if current_chr == "X":
                X_points.append(self)
                current_chr = "O"
                self.status_label.configure(text="O's turn")
            elif current_chr == "O":
                O_points.append(self)
                current_chr = "X"
                self.status_label.configure(text="X's turn")

        self.check_win()
        if play_with == "Computer" and self.status_label['text'] == "O's turn":
            self.auto_play()

    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == "X":
            X_points.remove(self)
        elif self.value == "O":
            O_points.remove(self)
        self.value = None
