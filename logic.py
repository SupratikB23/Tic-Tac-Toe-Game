from board import XO_points, X_points, O_points
import tkinter as tk

class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def check(self, for_chr):
        self.p1_satisfied = self.p2_satisfied = self.p3_satisfied = False
        points = X_points if for_chr == "X" else O_points
        for point in points:
            if point.x == self.x1 and point.y == self.y1:
                self.p1_satisfied = True
            elif point.x == self.x2 and point.y == self.y2:
                self.p2_satisfied = True
            elif point.x == self.x3 and point.y == self.y3:
                self.p3_satisfied = True
        return all([self.p1_satisfied, self.p2_satisfied, self.p3_satisfied])

winning_possibilities = [
    WinningPossibility(1,1,1,2,1,3),
    WinningPossibility(2,1,2,2,2,3),
    WinningPossibility(3,1,3,2,3,3),
    WinningPossibility(1,1,2,1,3,1),
    WinningPossibility(1,2,2,2,3,2),
    WinningPossibility(1,3,2,3,3,3),
    WinningPossibility(1,1,2,2,3,3),
    WinningPossibility(3,1,2,2,1,3)
]

def disable_game():
    from ui import play_again_button, status_label
    for point in XO_points:
        point.button.configure(state=tk.DISABLED)
    play_again_button.pack()

def check_win():
    from ui import status_label
    for possibility in winning_possibilities:
        if possibility.check('X'):
            status_label.configure(text="X won!")
            disable_game()
            return
        elif possibility.check('O'):
            status_label.configure(text="O won!")
            disable_game()
            return
    if len(X_points) + len(O_points) == 9:
        status_label.configure(text="Draw!")
        disable_game()
