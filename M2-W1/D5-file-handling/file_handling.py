import re

# File Handling Basics
# Write a new text file. 
# If the file exists, its content is overwritten.
file = open('monty_python.txt', 'w') # w stands for write mode
file.write("Arthur, King of the Britons\n")
file.write("Sir Lancelot, the Brave\n")
file.write("Sir Galahad, the Pure\n")
file.write("Sir Robin, the Not-Quite-So-Brave-as-Sir-Lancelot\n")
file.write("Tim, the Enchanter\n")
file.close() # Ensures the file is saved and resources are freed


# a is append mode
# this will add to the file, not overwrite it
with open("monty_python.txt", "a") as file:
    file.write("White Rabbit, The Destroyer")
    
    
# "with open" lets us to create the file var and open and close the file all in one
#   always use "with open"
# r is read mode
# read() - grabs everything in the txt file and returns it as a string
with open('monty_python.txt', 'r') as file:
    contents = file.read()
    print("\n--- monty_python.txt contents: ---")
    print(contents)
    
    
# Loop through line by line
print("\n----Line by Line----")
with open("monty_python.txt", "r") as file:
    for line in file:
        print(line.strip())
        

# Write data from a Python list to a file
knights = [
    "Sir Bedevere, The Wise",
    "The Black Knight, Limbless",
    "French Taunter, The Ruthless"
]
    
with open('new_knights.txt', 'w') as file:
    for knight in knights:
        file.write(knight + '\n')   
    
# Fancy way
# .join converts list into a string
# each item in list will have a \n before it
with open('new_knights.txt', 'a') as file:
    file.write("\n".join(knights))
    

# Read data from the file into a list
list_of_knights = []

with open('new_knights.txt', 'r') as file:
    for line in file:
        list_of_knights.append(line.strip())
print("\n--- Knights from File With For In ---")
print(list_of_knights)


# Fancy way
# readlines() converts each line in the txt file to an item in a list
with open('new_knights.txt', 'r') as file:
    knight_list = file.readlines()
    print("\n--- Knights from File With readlines() ---")
    
    # list comprehension
    # loops through knight_list strips each line and creats a list all in one
    print([line.strip() for line in knight_list])
    

# Write data from a Python dictionary to a file
castle_info = {
    "Camelot": "It's only a model.",
    "Castle Anthrax": "Not a very good name.",
    "Castle of Aaaaargh": "An unpronounceable name."
}
with open('castle_info.txt', 'w') as file:
    for castle, description in castle_info.items():
        file.write(f"{castle}: {description}\n")


# Read data from a file into a dictionary
with open('castle_info.txt', 'r') as file:
    castle_dict = {}
    for line in file:
        #unpacking
        castle, description = line.strip().split(": ", 1) # only splits once
        castle_dict[castle] = description
    print("\n--- Castle Dictionary ---")
    print(castle_dict)
    
# Regex Example: Group items from a file
# Patter is "Sir " folowed by one or more word characters
#   followed by ", the " and then one or more word characters
# It puts the two word characters into groups (tuples)
# .findall() takes all the matched groups and puts them in a list
# .read() - reads the entire content of a file and returns it as a single string
pattern = r"Sir (\w+), the (\w+)"
with open('monty_python.txt', 'r') as file:
    matches = re.findall(pattern, file.read())
    print("\n--- Regex Groups ---")
    print(matches)  # [('Lancelot', 'Brave'), ('Galahad', 'Pure'), ('Robin', 'Not-Quite-So-Brave-as-Sir-Lancelot')]
