import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", font=("Arial", 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        
        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=1)
        
    def make_move(self, row, col):
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()
    
    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False
    
    def check_tie(self):
        return all(self.buttons[i][j]['text'] != "" for i in range(3) for j in range(3))
    
    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
        self.current_player = "X"
    
    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)
    
    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()