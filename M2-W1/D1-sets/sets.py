"""
In Python, a set is an unordered collection of unique elements. 
It is defined using curly braces {} or the set() constructor. 

Key Characteristics of Sets:
Unique Elements: A set automatically removes duplicate elements.
Unordered: The elements in a set do not have a defined order 
    and cannot be accessed by index.
Mutable: Sets themselves can be modified (adding or removing elements), 
    but the elements in a set are immutable (e.g., numbers, strings, tuples).
    
Common uses: removing duplicates, checking memberships (emails, ips, usernames),
    tracking unique visits to a website, checking password against set of
    commonly used passwords, game inventories, etc
"""

fellowship = set()

fellowship.add("Frodo")
fellowship.add("Sam")
fellowship.add("Gandalf")
fellowship.add("Aragorn")

print(f"The Fellowship of the Ring: {fellowship}")

heroes = {"Legolas", "Gimli", "Gandalf"}

print("\nIs Legolas in the fellowship?", "Legolas" in fellowship)
print("\nIs Legolas in the fellowship?", "Legolas" in heroes)

# Validation of Membership or Inclusion: 
# Is my group (heroes) a part of their group (fellowship)"
# Use issubset() to ensure that a smaller collection (heroes) 
# is fully satisfied by a larger collection (fellowship).
# Examples - graduation requirements | read/write permissions
print("\nAre all heroes in the fellowship?", heroes.issubset(fellowship))

# Containment or Ownership Testing
# Does my group (fellowship) contain their group (heroes)?
# Use issuperset() to confirm that one set (fellowship) 
# includes all elements of another (heroes)
# Examples - catalog of items | making sure a catalog contains all items
print("Does the fellowship contain all the heroes?", fellowship.issuperset(heroes))

"""
Summary Analogy:
issubset(): "Do my skills meet the job requirements?"
issuperset(): "Does my toolbox contain all the tools needed for the task?"
"""

# Add a duplicate list of hobbits and remove duplicates using a set
hobbits_list = ["Frodo", "Sam", "Merry", "Pippin", "Frodo", "Sam"]
unique_hobbits = set(hobbits_list)
print(f"\nUnique hobbits after removing duplicates: {unique_hobbits}")

# Intersection: Characters who are both in the fellowship and heroes
heroes_in_fellowship = fellowship.intersection(heroes)
print("\nHeroes in the Fellowship of the Ring:", heroes_in_fellowship)

# Union: Combines all items from two sets into one leaving out the duplicates
all_characters = fellowship.union(heroes)
print(f"\nAll characters (Fellowship + Heroes): {all_characters}")

# Difference: Heroes who are not in the fellowship
heroes_not_in_fellowship = heroes.difference(fellowship)
fellowship_not_in_heroes = fellowship.difference(heroes)
print("\nHeroes not in the Fellowship of the Ring:", heroes_not_in_fellowship)
print("\nFellowship not in heroes:", fellowship_not_in_heroes)

# Symmetric Difference: Characters who are either in the fellowship or heroes, but not both
unique_to_each_set = fellowship.symmetric_difference(heroes)
print("\nCharacters unique to either the Fellowship or Heroes:", unique_to_each_set)

# Loop over the fellowship
print("\nFellowship members:")
for member in fellowship:
    print(member)

# Remove a member from the fellowship
fellowship.discard("Boromir")  # no error
fellowship.discard("Sam")
print(f"\nAfter Sam leaves the Fellowship: {fellowship}")

# Frozen set example: Immutable set for the three Elven Rings
weapons = frozenset(["Sting", "Narsil", "Andúril"])
print("\nWeaopons (frozen set):", weapons)
# weapons.add("The Ring") # causes error