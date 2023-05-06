from colored import fg, attr

from clear import clear


# Story 3 questions/prompts

s3_topic = input("You have to give an impromptu speech in 5 minutes, what topic would you speak about?: ")
s3_room = input("Name a room in your house: ")
s3_snack = input("What is your least favourite food of all time?: ")
s3_vessel = input("Name a type of vessel to hold a liquid: ")
s3_drink = input("What is your favourite beverage?: ")
s3_animal = input("What is your favourite animal?: ")

clear()

# Story 3 - The Student

print(f"{fg('red')}THE STUDENT{attr('reset')}")
madlib3 = (f"It's late and you're pulling another all-nighter.\nYou have a big project due Sunday May 7th on the topic of {s3_topic} and you really need to study.\nIt's important to stay awake and focus so you go to the {s3_room} and grab yourself a big bowl of {s3_snack} and another {s3_vessel} of {s3_drink} for energy.\nYou have had enough {s3_drink} to stay awake for days!\nIt feels as though only an hour has passed but the sun has risen and you can hear the {s3_animal} sing.\nYou have managed to stay up all night and successfully finish your assignent on {s3_topic}!")

print(madlib3)