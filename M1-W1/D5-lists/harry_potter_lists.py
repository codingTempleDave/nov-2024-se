# LISTS (ARRAYS)
inventory = ["wand", "invisibility cloak", "marauder's map", "Nimbus 2000"]

print(f"First item: {inventory[0]}")
print(f"Third item: {inventory[2]}")
print(f"Last item: {inventory[-1]}")

# mixed lists and adding items
inventory.append(9.75) # adds it to the end of the list
inventory.append("golden snitch")
print(f"\nAdded 9.75 and then golden snitch to the end: {inventory}")
inventory.insert(2, "howler letter") # places this in the index of 2 (3rd)
print(f"\nAdded howler letter at position 2: {inventory}")

# Removing items
inventory.remove("invisibility cloak") # list functions
print(f"Removed invisibility cloak: {inventory}")

del inventory[1]
print(f"Deleted item at index 1: {inventory}")

# Removing and retrieving the last item with pop()
last_item = inventory.pop()
print(f"\nPopped the last item: {last_item}")
print(f"Inventory after pop: {inventory}")

# Extending the inventory with more magical items
more_items = ["philosopher's stone", "butter beer"]
inventory.extend(more_items) # combine lists
print(f"\nExtended inventory: {inventory}")

# Slicing
print(f"\nFirst three items: {inventory[:3]}")
print(f"Last two items: {inventory[-2:]}")
print(f"2nd and 3rd items {inventory[1:3]}")

# Nested lists
inventory.append(["expelliarmus", "expecto patronum", "lumos"])
inventory.append(["jewels", "rubies", "gold"])
print(f"\nAdded spell list to inventory: {inventory}")
print(f"First spell: {inventory[6][0]}") 
print(f"Third spell: {inventory[-1][2]}")
print(f"Rubies: {inventory[7][1]}")
print(f"Expecto Patronum: {inventory[6][1]}")

# Finding the length of the list
print(f"\nTotal items in inventory: {len(inventory)}")


# Looping through the inventory list
print("\nLooping through Harry's inventory:")
for item in inventory: # item - temporary var that exists only in the loop
    print(f"- {item}")
    
print("\nLooping through every item of Harry's inventory:")
for item in inventory:
    if isinstance(item, list): # checking to see if item is a list
        for nested_item in item:
            print(f"- {nested_item}")
    
    else:            
        print(f"- {item}")
        
        
# Clearing the inventory
inventory.clear()
print(f"\nInventory cleared: {inventory}")


# Numeric operations on a list of potion quantities (fictional)
potion_quantities = [7, 12, 3, 5]
print(f"\nMin potion quantity: {min(potion_quantities)}")
print(f"Max potion quantity: {max(potion_quantities)}")


# Sorting and reversing potion quantities
potion_quantities.sort()
print(f"\nSorted potion quantities: {potion_quantities}")
potion_quantities.reverse()
print(f"Reversed sorted potion quantities: {potion_quantities}")