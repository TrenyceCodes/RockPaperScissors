from tkinter import *
from PIL import ImageTk, Image

GameRoot = Tk()
GameForm = Frame(GameRoot, padx=10, pady=10)
GameForm.grid()
Label(GameForm, text="Hello world").grid(column=0, row=0)
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

Button(GameRoot, image=rock_photo, width=220, height=220, pady=20).grid(column=0, row=2)
Button(GameRoot, image=scissors_photo, width=220, height=220, pady=20).grid(column=1, row=2)
Button(GameRoot, image=paper_photo, width=220, height=220, pady=20).grid(column=2, row=2)
Button(GameForm, text="Exit Game", command=GameRoot.destroy).grid(column=0, row=1)
GameRoot.mainloop()