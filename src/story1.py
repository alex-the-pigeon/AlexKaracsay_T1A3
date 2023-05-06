from colored import fg, attr

from clear import clear
# Story 1 questions/prompts

s1_venue = input("Name a type of venue: ")
s1_dancemove = input("Name a dance move: ")
s1_vehicle = input("Name a type of vehicle: ")
s1_emotion = input("You're about to see your favourite band play, how do you feel?: ") 
s1_fictional_character = input("Enter the name of a fictional character: ")
s1_movement = input("Enter a type of movement eg. dance, run etc. : ")
s1_sound = input("Name a sound eg. scream, burp etc. : ")
s1_adjective = input("Enter a silly adjective: ")

clear()
# Story 1 - The Comedian

print(f"{fg('green')}THE COMEDIAN{attr('reset')}")
madlib1 = (f"You're heading out the door to see your favourite comedian perform at the grand {s1_venue}.\nYou {s1_dancemove} over to the street and get in your {s1_vehicle} to drive to the show.\nSoon you arrive at the {s1_venue}.\nTicket in hand, you show it to the usher and head inside.\nThe sound of the crowd starts to swell.\nEveryone is very {s1_emotion} about seeing the latest stand-up show by {s1_fictional_character}.\nYou {s1_movement} over to your seat in the front row and sit down.\nThe show is about to start and you're so feeling so {s1_emotion}.\n{s1_fictional_character} comes out on stage and begins to {s1_sound} loudly.\nThe crowd applauds.\nWhat an {s1_adjective} show!")

print(madlib1)

     
