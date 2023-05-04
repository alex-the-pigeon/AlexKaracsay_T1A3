# import information here
from functions import story1, story2, story3 


# ASCII art header



# Beginning of menu function 
print("Welcome to SILLY LIBS, a SILLY game with SILLY jokes for SILLY fun!")


def create_menu():
    print("| Enter 1 to choose:  THE COMEDIAN |")
    print("| Enter 2 to choose:  THE ATHLETE  |")
    print("| Enter 3 to choose:  THE STUDENT  |")
    print("| Enter 4 to to return to menu     |")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""


while user_choice != "4":
    user_choice = create_menu()

    if (user_choice == "1"):
        story1()
    elif (user_choice == "2"):
        story2()
    elif (user_choice == "3"):
        story3()
    elif (user_choice == "4"):
        continue
    else:
        print("Invalid Input")

    input("Press ENTER to continue")

print("Thank you for playing SILLY LIBS!")   





