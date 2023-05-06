from colored import fg, attr

from clear import clear

# Story 2 questions/prompts

s2_activity = input("What is one of your favourite activities?: ")
s2_number = input("What is your age?: ")
s2_clothing = input("Tell me the colour and item of clothing you are wearing: ")
s2_sound = input("Name a sound: ")
s2_movement = input("Enter a type of movement eg. dance, run etc. : ")
s2_adjective = input("Enter an adjective:  ") 
s2_colour = input("What is your least favorite colour?: ")

clear()
# Story 2 - The Athlete

print(f"{fg('yellow')}THE ATHLETE{attr('reset')}")
madlib2 = (f"You have been training for what seems like eternity but you are finally here.\nIt's the Olympic Games and you're ready to represent your country in {s2_activity}.\nYou're standing in a packed-out stadium of {s2_number} people and you are at the starting line in your {s2_clothing}.\nThe other athletes line up beside you and the gun goes off which makes a loud {s2_sound}.\nYou start to {s2_movement} and you're suddenly in the lead.\nThe other athletes cannot keep up with your {s2_adjective} skills.\nYou fly across the finish line and win the {s2_colour} medal in the prestigious sport of {s2_activity}!")

print(madlib2)