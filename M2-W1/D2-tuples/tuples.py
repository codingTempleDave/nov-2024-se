"""
Tuples
-Ordered: The elements in a tuple maintain their position and can be accessed using indices.
-Immutable: You cannot change, add, or remove items in a tuple after it is created.
-Heterogeneous: Tuples can contain a mix of data types.
-Defined by Parentheses: Tuples are typically created using () or the tuple() constructor.
-Memory efficient: Tuples are more memory efficient than lists
-Read only integrity: once they've been created the data can't change
-Common uses: fixed coordiantes on a map, sensitive data from databases that should not change
"""

# Creating a tuple with names of the Fellowship
fellowship = ("Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Gimli")
print(f"The Fellowship of the Ring: {fellowship}")

# Single element tuple (requires a trailing comma)
ring_bearer = ("Frodo",)
print(f"\nRing Bearer (single element tuple): {ring_bearer}, Type: {type(ring_bearer)}")

# Empty tuple
empty_council = ()
print(f"\nAn empty council: {empty_council}, Type: {type(empty_council)}")

# Using the tuple() constructor
elven_gifts = tuple(["Lembas Bread", "Elven Cloak", "Light of Eärendil"])
print(f"\nElven gifts from Galadriel: {elven_gifts}")

# Accessing tuple elements
print(f"\nLeader of the Fellowship: {fellowship[2]}")

# Slicing tuples
print(f"\nFirst four members of the Fellowship: {fellowship[0:4]}")
print(f"\nLast four members of the Fellowship: {fellowship[-4:]}")

# Looping over tuples
print("\nMembers of the Fellowship:")
for member in fellowship:
    print(f"- {member}")
    
# Tuples are immutable; attempting to change an element raises an error
try:
    fellowship[0] = "Smaug"  # This will fail, we don't want Smaug (:
except TypeError as e:
    print(f"\nCannot modify tuple: {e}")
    

# Reassigning a tuple
fellowship = ("Frodo", "Sam", "Aragorn", "Galadriel", "Merry", "Pippin", "Boromir")
print(f"\nUpdated Fellowship: {fellowship}")


# Tuple packing and unpacking
# Great for csv (comma separated values) files
weapons = "Andúril", "Bow of Galadriel", "Gimli's Axe"
print(f"\nPacked weapons: {weapons}")
sword, bow, axe = weapons # "Andúril", "Bow of Galadriel", "Gimli's Axe"
print(f"Unpacked weapons: Sword: {sword} | Bow: {bow} | Axe: {axe}")


# Extended unpacking
first, *middle, last = fellowship
print(f"\nFirst: {first}, Middle members: {middle}, Last: {last}")


# Using _ as a placeholder in unpacking
_, _, third_member, *_ = fellowship
print(f"\nThird member of the Fellowship (using placeholder): {third_member}")


# Unpacking and packing with functions/parameters/arguments
def introduce_member(name, role, origin):
    print(f"\n{name}, the {role}, hails from {origin}.")

def list_roles(*members):
    print("\nRoles in the Fellowship of the Ring:")
    for name, role, _ in members:
        print(f"- {name}: {role}")

frodo = ("Frodo", "Ring-bearer", "Shire")
gandalf = ("Gandalf", "Wizard", "Valinor")

introduce_member(*frodo)
introduce_member(*gandalf)

list_roles(frodo, gandalf)


# Tuple methods: count() and index()
print(f"\nCount of 'Sam' in Fellowship: {fellowship.count('Sam')}")
print(f"Index of 'Aragorn' in Fellowship: {fellowship.index('Aragorn')}")


# Tuples as dictionary keys
locations = {
    (34.0522, -118.2437): "The Shire",
    (40.7128, -74.0060): "Mount Doom",
    (51.5074, -0.1278): "Rivendell"
}
print(f"\nDestination: {locations[(40.7128, -74.0060)]}")
print(f"\nDestination: {locations[(34.0522, -118.2437)]}")