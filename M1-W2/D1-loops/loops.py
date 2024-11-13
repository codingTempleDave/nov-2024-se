characters = [
    "Luke Skywalker",
    "Darth Vader",
    "Yoda",
    "Leia Organa",
    "Han Solo",
    "Emperor Palpatine",
    "Chewbacca",
]

for i in range(0, len(characters)):
    print(f"{i + 1} - {characters[i]}")  # i is the index position

print("-" * 30)

# enumerate separates index and value
for index, name in enumerate(characters):
    print(f"{index + 1} - {name}")

print("-" * 30)

for character in characters:
    print(character)

print("-" * 30)

print("Preparing for light speed jump!")
for second in range(5, 0, -1):
    print(f"{second}...")
print("light speed activated!  VROOOM!!!!")

print("-" * 30)

print("Who will bring balance to the force?")
for character in characters:
    if character == "Darth Vader":
        print(f"{character} brought balance to the force but at a great cost 😢")
    elif character == "Emperor Palpatine":
        print(f"{character} is pure evil.  He will not balance anything!")
    else:
        print(f"{character} is probably an ally")

print("-" * 30)


weapons = ["lightsaber", "force choke", "force push", "blaster"]

for weapon, character in zip(weapons, characters):
    # secret = "Keep it secret keep it safe"
    print(f"{weapon} protects {character}")

tracker = True
while tracker:
    print("This will blow up the world")
    tracker = False


force_level = 0
target_force_level = 10

print("Jedi training started....")
while True:
    print(f"Force level: {force_level}. Training intensifies!!")
    force_level += 1
    if force_level == 3:
        print("You can lift rocks!  You feel the force growing stronger!")
        continue  # stops the current iteration and runs the loop again
    if force_level == 6:
        print(
            "You can lift your space ship and do front flips with Yoda " "on your back!"
        )
        continue
    elif force_level == target_force_level:
        print("Training complete! You are now a Jedi Knight, Yoda is pleased")
        break

print("-" * 30)

import random

# Nested for loop to simulate a battle between two teams
jedi_team = ["Luke Skywalker", "Yoda", "Obi-Wan Kenobi"]
rebel_team = ["Leia Organa", "Han Solo", "Chewbacca"]

print("Jedi Sparring Simulation!")
for jedi in jedi_team:
    for rebel in rebel_team:
        print(f"{jedi} engages in a duel with {rebel}!")
        if rebel == "Leia Organa" and jedi == "Luke Skywalker":
            print("Luke can't fight his sister, but he can kiss her... 😯")
        else:
            rebel_attack = random.randint(0, 10)
            if jedi == "Yoda":
                jedi_attack = 100
            else:
                jedi_attack = random.randint(0, 10)

            print(
                f"{jedi}'s attack: {jedi_attack} \n" 
                f"{rebel}'s attack: {rebel_attack}"
            )

            (
                print(f"{rebel} is victorious") 
                if rebel_attack >= jedi_attack
                else print((f"{jedi} is victorious"))
            )

    print(f"{jedi} is done dueling.  The next Jedi is up\n")
