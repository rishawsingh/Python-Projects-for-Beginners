# Original: Python Dice Rolling Game using Tkinter
#                                 - Rishaw Kumar
# Dice Roller
# New functionality added by Michael Connell 

from tkinter import *
import random

App = Tk()
App.title("Dice Roller")

# Dice unicode characters dictionary (for six-sided dice)
Dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

# First dice character to show when the app starts
lbl = Label(App, text=Dice[0], font=('Times', 100))
lbl.grid(row=0, column=0, padx=40)

# Commenting out the original roll function
# def roll():
#     from random import randint
#     dice_choice = randint(1, 6)
#     dice_lbl = Label(App, text=Dice[dice_choice], font=('Times', 100), width=2)
#     dice_lbl.grid(row=0, column=0, padx=40)

# New Feature: Roll Different Types of Dice
def roll_dice(dice_type):
    # This function generates a random number based on the dice type selected
    return random.randint(1, dice_type)

def roll():
    # Retrieve the selected dice type from the dropdown
    dice_type = int(dice_type_var.get())
    roll_result = roll_dice(dice_type)
    
    # Update the label with the new roll result (limited to six-sided dice representation)
    lbl.configure(text=Dice.get(roll_result, Dice[0]))

# Dropdown menu for selecting dice type
dice_type_var = StringVar(App)
dice_type_var.set("6")  # default value
dice_type_menu = OptionMenu(App, dice_type_var, "4", "6", "8", "10", "12", "20")
dice_type_menu.grid(row=1, column=0)

# Roll button
roll_button = Button(App, text='Roll', command=roll)
roll_button.grid(row=2, column=0)

App.mainloop()
