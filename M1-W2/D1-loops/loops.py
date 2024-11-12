characters = [ "Luke Skywalker", "Darth Vader", "Yoda", "Leia Organa", 
               "Han Solo", "Emperor Palpatine", "Chewbacca"]

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

print('Who will bring balance to the force?')
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
