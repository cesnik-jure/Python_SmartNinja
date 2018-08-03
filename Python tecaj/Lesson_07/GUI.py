import tkinter
from tkinter import messagebox
import random


window = tkinter.Tk()
greeting = tkinter.Label(window, text="Guess the secret number!")

secret = random.randint(1, 100)
guess = tkinter.Entry(window)

def check_guess(event = False):
    print(secret)
    user_guess = int(guess.get())
    print(user_guess)
    if user_guess == secret:
        text = ("Correct guess.")
    else:
        text = "Wrong guess."

    messagebox.showinfo("Result", text)

guess.bind('<Return>', check_guess)

submit = tkinter.Button(window, text = "Guess", command = check_guess)

greeting.pack()
guess.pack()
submit.pack()

window.mainloop()