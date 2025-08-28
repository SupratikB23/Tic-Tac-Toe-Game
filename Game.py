import tkinter as tk
from ui import setup_ui

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Tic Tac Toe")
    setup_ui(root)
    root.mainloop()
