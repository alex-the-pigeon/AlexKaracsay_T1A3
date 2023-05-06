# imports
#From functions file to run each story
from functions import story1, story2, story3 , story4
# Colored 1.4.4 package
from colored import fg, bg, attr
# Art 5.9 package
from art import *
# Clear  2.0.0 screen package
from clear import clear

# ASCII art header

tprint("SILLY  LIBS!!!","wizard") #This "wizard" code randomly selects an appropriate font to correspond with how much text is written. It will change every time the program is run for a bit of fun.

# Welcome title print
print(f"{fg('blue')}{attr('bold')}Welcome to SILLY LIBS, a SILLY game with SILLY jokes for SILLY fun!{attr('reset')}")

# Beginning of menu function 
def create_menu():
    print(f"{fg('green')}| Enter 1 to choose:  THE COMEDIAN | {attr('reset')}")
    print(f"{fg('yellow')}| Enter 2 to choose:  THE ATHLETE  | {attr('reset')}")
    print(f"{fg('red')}| Enter 3 to choose:  THE STUDENT  | {attr('reset')}")
    print(f"{fg('purple_3')}| Enter 4 to choose:  THE MAGICIAN |{attr('reset')}")          
    print(f"{fg('cyan')}{attr('bold')}| Enter 5 to exit     |{attr('reset')}")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

# Menu loop - Only numbers 1 through 5 will work, any other value will throw an error and tell the user that their choice is invalid.
while user_choice != "5":
    user_choice = create_menu()

    if (user_choice == "1"):
        story1()  # These are referencing the separate story files that are also in the functions file
    elif (user_choice == "2"):
        story2()
    elif (user_choice == "3"):
        story3()
    elif (user_choice == "4"):
        story4()
    elif (user_choice == "5"):
        continue # If 5 is chosen it will keep the program running and await further input
    else:
        print("Invalid Input")

    input("Press ENTER to play again") #This will appear at the bottom of the terminal in the menu and also in each story so the user can easily get back to the menu and play again.
    clear()

print(f"{bg('blue')}Thank you for playing SILLY LIBS!{attr('reset')}")  



