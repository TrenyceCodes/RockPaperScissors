#system goal to 3
import random
from tkinter import *
from PIL import ImageTk, Image

#let ai pick a random game option
#user can pick a choice by input

#check if users decision beats ai decision
#if user picked rock and ai picked scissors, user wins
#if user picked paper and ai picked rock, user wins
#if user picked scissors and ai picked paper, user wins
#vice versus for ai choosing rock, paper, scissors

#sets up root and title
GameRoot = Tk()
GameRoot.title("Rock Paper Scissors Game")
GameRoot.resizable(True, True)

#sets up game system
user_points: int = 0
ai_points: int = 0
game_match: int = 3
ai_options = ["rock", "paper", "scissors"]


#handles who is the winner of the game
def handle_winner(user_choice: str):
    global user_points, ai_points
    ai_decision = random.choice(ai_options)

    print(f"Users decision: {user_choice}")
    print(f"Ai decision: {ai_decision}")

    #runs if loop to check for multiple decisions
    if user_choice == ai_decision:
        print(f"It's a draw! Pick another choice")
    elif (user_choice == "rock" and ai_decision == "scissors") or \
            (user_choice == "paper" and ai_decision == "rock") or \
            (user_choice == "scissors" and ai_decision == "paper"):
        print(f"{user_choice} beats {ai_decision}")

        user_points += 1
    else:
        print(f"{ai_decision} beats {user_choice}")
        ai_points += 1

    print(f"Current Score - User Score: {user_points} - AI score: {ai_points}")

    if user_points == game_match:
        print(f"User has won the match: {user_points}")
        reset_game()
    else:
        print(f"Ai has won the match: {ai_points}")
        reset_game()


#resets the game
def reset_game():
    global user_points, ai_points
    ai_points = 0
    user_points = 0


GameForm = Frame(GameRoot, padx=10, pady=10)
GameForm.grid()
(rock_image,
 scissors_image,
 paper_image) = (
    Image.open("rock.jpeg"),
    Image.open("scissors.jpeg"),
    Image.open("paper.jpeg"))

(rock_photo,
 scissors_photo,
 paper_photo) = (
    ImageTk.PhotoImage(rock_image),
    ImageTk.PhotoImage(scissors_image),
    ImageTk.PhotoImage(paper_image))

Label(GameRoot, text=f"Your Score: {user_points}").grid(column=0, row=0)
Label(GameRoot, text=f"AI Score: {ai_points}").grid(column=3, row=0)
Button(GameRoot, image=rock_photo, command=lambda: handle_winner("rock"), width=220, height=220, pady=20).grid(column=0,
                                                                                                               row=1)
Button(GameRoot, image=scissors_photo, command=lambda: handle_winner("scissors"), width=220, height=220, pady=20).grid(
    column=1,
    row=1)
Button(GameRoot, image=paper_photo, command=lambda: handle_winner("paper"), width=220, height=220, pady=20).grid(
    column=3,
    row=1)
Button(GameRoot, text="Exit Game", command=GameRoot.destroy).grid(column=1, row=0)
GameRoot.mainloop()
