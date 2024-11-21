# Create a basic dictionary representing the Fellowship of the Ring
fellowship = {
    #key      #value
    "Frodo": "Ring-bearer",
    "Aragorn": "Ranger of the North",
    "Legolas": "Elf of Mirkwood",
    "Gimli": "Dwarf of Erebor",
    "Boromir": "Man of Gondor",
    "Sam": "Gardener",
}

# Accessing a value by key
print(f"Frodo's role: {fellowship['Frodo']}")
#print(f"Galadriel's role: {fellowship['Galadriel']}")

# Using .get() to safely access keys
print(f"Galadriel's role: {fellowship.get('Galadriel')}")
print(f"Galadriel's role: {fellowship.get('Galadriel', 'Not in the fellowship')}")

# Adding a new member
fellowship["Merry"] = "Hobbit of the Shire"
print("\nAfter adding Merry:", fellowship)

# Removing a member using .pop()
removed = fellowship.pop("Boromir")
print("\nRemoved Boromir:", removed)
print("After removing Boromir:", fellowship)

# Removing a member using del
del fellowship["Sam"]
print("\nAfter removing Sam with del:", fellowship)

# Modifying an element in a dictionary
fellowship["Legolas"] = "Prince of Mirkwood"
print("\nAfter modifying Legolas's role:", fellowship)

# .keys(), .values(), and .items()
print("\nMembers (keys):", fellowship.keys())
print("Roles (values):", fellowship.values())
print("Members and roles (items):", fellowship.items())

# Looping through the dictionary
print("\nLooping through dictionary:")
# gives me the keys
for member in fellowship:
    print(f"{member}")
# gives me the values    
for member in fellowship:
    print(f"{fellowship[member]}")
    
# Looping through the dictionary with items()
print("\nLooping through dictionary using items():")
for member, role in fellowship.items():
    print(f"{member}: {role}")
    
# Looping using .keys() and .values()
print("\nLooping using keys():")
for member in fellowship.keys():
    print(f"Member: {member}")

print("\nLooping using values():")
for role in fellowship.values():
    print(f"Role: {role}")
    
# Nested dictionaries
middle_earth = {
    "Fellowship": fellowship,
    "Enemies": {
        "Saruman": "Corrupted Wizard",
        "Sauron": "Dark Lord",
        "Orcs": "Creatures of Mordor"
    },
}

# Accessing nested dictionaries
print("\nSauron's title:", middle_earth["Enemies"]["Sauron"])
print("\nFrodo's title:", middle_earth["Fellowship"]["Frodo"])

# Modifying a nested dictionary
middle_earth["Enemies"]["Saruman"] = "Traitorous Wizard"
print("\nAfter modifying Saruman's title:", middle_earth["Enemies"])

# Adding to a nested dictionary
middle_earth["Enemies"]["Gollum"] = "Ring Obsessed Hobbit"
print("\nAfter adding Gollum to enemies:", middle_earth["Enemies"])

# Looping through a nested dictionary
print("\nLooping through Enemies:")
for enemy, title in middle_earth["Enemies"].items():
    print(f"{enemy}: {title}")
    
# List inside of a dictionary
middle_earth["Allies"] = ["Ents", "Elves", "Dwarves", "Men"]
print(middle_earth)
# Accessing a list inside a dictionary
print("\nAllies of Middle-earth:", middle_earth["Allies"])
print(f"\nElves: {middle_earth["Allies"][1]}")

# Looping through a list inside a dictionary
print("\nLooping through Allies:")
for ally in middle_earth["Allies"]:
    print(f"Ally: {ally}")
    
    
# List of dictionaries
armies = [
    {"Name": "Rohan", "Leader": "Theoden", "Strength": "Cavalry"},
    {"Name": "Gondor", "Leader": "Denethor", "Strength": "Infantry"},
    {"Name": "Mordor", "Leader": "Sauron", "Strength": "Orcs"},
]

# Accessing data in a list of dictionaries

print("\nLeader of Mordor:", armies[2]["Leader"])
print("\nLeader of Rohan:", [army["Leader"] for army in armies if army["Name"] == "Rohan"][0])

# Loop through a list of dictionaries
print("\nArmies and their strengths:")
for army in armies:
    print(f"{army['Name']} led by {army['Leader']} specializes in {army['Strength']}.")