# import information here
from functions import story1, story2, story3 , story4


# ASCII art header



# Welcome title print
print("Welcome to SILLY LIBS, a SILLY game with SILLY jokes for SILLY fun!")

# Beginning of menu function 
def create_menu():
    print("| Enter 1 to choose:  THE COMEDIAN |")
    print("| Enter 2 to choose:  THE ATHLETE  |")
    print("| Enter 3 to choose:  THE STUDENT  |")
    print("| Enter 4 to choose:  THE MAGICIAN |")
    print("| Enter 5 to to return to menu     |")
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

    input("Press ENTER to continue") #This will appear at the bottom of the terminal in the menu and also in each story so the user can easily get back to the menu and play again.

print("Thank you for playing SILLY LIBS!")   





