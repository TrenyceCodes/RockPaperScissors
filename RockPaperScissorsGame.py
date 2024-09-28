import random
from tkinter import *
from tkinter import messagebox

GameRoot = Tk()

class RockPaperScissorsGame:
    user_points: int
    ai_points: int
    game_match: int
    ai_options: list[str]
    widget_width_height: int

    def __init__(self, game_root: Tk):
        self.game_root = game_root
        self.game_root.title("Rock Paper Scissors Game")
        self.game_root.resizable(False, False)

        self.user_points = 0
        self.ai_points = 0
        self.game_match = 3
        self.widget_width_height = 20
        self.ai_options = ["rock", "paper", "scissors"]

        self.handle_managing_widgets()

    def handle_managing_widgets(self):
        self.user_score_label = Label(GameRoot, text=f"Your Score: {self.user_points}")
        self.user_score_label.grid(column=0, row=0)

        self.ai_score_label = Label(GameRoot, text=f"AI Score: {self.ai_points}")
        self.ai_score_label.grid(column=3, row=0)

        self.current_score_label = Label(GameRoot, text=f"Current Score - User Score: {self.user_points} - AI score: {self.ai_points}")
        self.current_score_label.grid(column=1, row=2)

        self.ai_decision_label = Label(GameRoot, text=f"AI chose: ")
        self.ai_decision_label.grid(column=3, row=2)

        self.user_decision_label = Label(GameRoot, text=f"You chose: ")
        self.user_decision_label.grid(column=0, row=2)

        self.result_label = Label(GameRoot, text=f"")
        self.result_label.grid(column=1, row=4)

        Button(GameRoot, text="Rock", command=lambda: self.handle_winner("rock"), width=self.widget_width_height, height=self.widget_width_height).grid(
            column=0,
            row=1)
        Button(GameRoot, text="Scissors", command=lambda: self.handle_winner("scissors"), width=self.widget_width_height,
               height=self.widget_width_height).grid(
            column=1,
            row=1)
        Button(GameRoot, text="Paper", command=lambda: self.handle_winner("paper"), width=self.widget_width_height, height=self.widget_width_height).grid(
            column=3,
            row=1)
        Button(GameRoot, text="Exit Game", command=self.game_root.destroy).grid(column=1, row=0)

    def handle_winner(self, user_choice: str):
        ai_decision = random.choice(self.ai_options)

        print(f"Users decision: {user_choice}")
        print(f"Ai decision: {ai_decision}")
        self.user_decision_label.config(text=f"Users decision: {user_choice}")
        self.ai_decision_label.config(text=f"Ai decision: {ai_decision}")

        if user_choice == ai_decision:
            print(f"It's a draw! Pick another choice")
            self.result_label.config(text=f"It's a draw! Pick another choice")
        elif (user_choice == "rock" and ai_decision == "scissors") or \
                (user_choice == "paper" and ai_decision == "rock") or \
                (user_choice == "scissors" and ai_decision == "paper"):
            print(f"{user_choice} beats {ai_decision}")
            self.result_label.config(text=f"{user_choice} beats {ai_decision}")
            self.user_points += 1
            self.user_score_label.config(text=f"User Score: {self.user_points}")
        else:
            print(f"{ai_decision} beats {user_choice}")
            self.ai_points += 1
            self.ai_score_label.config(text=f"AI Score: {self.ai_points}")
            self.result_label.config(text=f"{ai_decision} beats {user_choice}")

        print(f"Current Score - User Score: {self.user_points} - AI score: {self.ai_points}")
        self.current_score_label.config(text=f"Current Score - User Score: {self.user_points} - AI score: {self.ai_points}")

        if self.user_points == self.game_match:
            print(f"User has won the match: {self.user_points}")
            messagebox.showinfo("Result", f"User has won the match: {self.user_points}")
            self.reset_game()

        if self.ai_points == self.game_match:
            print(f"Ai has won the match: {self.ai_points}")
            messagebox.showinfo("Result", f"AI has won the match: {self.ai_points}")
            self.reset_game()

    # resets the game
    def reset_game(self):
        self.ai_points = 0
        self.user_points = 0
        self.user_score_label.config(text=f"Your Score: 0")
        self.ai_score_label.config(text=f"AI Score: 0")


game = RockPaperScissorsGame(GameRoot)
GameRoot.mainloop()
