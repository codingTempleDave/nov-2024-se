import random

# classes should start with capital letter
class Character:
    # constructor function
    def __init__(self, name, race, strength, weapon, taunt):
        # attribute   parameter
        self.name = name
        self.race = race
        self.strength = strength
        self.weapon = weapon
        self.taunt = taunt
 
    def __str__(self):
        """String Representation Method - returns a string of the Character instance."""
        return (f"\n{self.name} ({self.race}) | Strength: {self.strength} | " 
                f"Weapon: {self.weapon} | Taunt: {self.taunt}")
    
    #instance method
    def attack(self):
        """Simulate an attack using print"""        
        print(f"\n{self.name} uses a {self.weapon} to attack with a power of "
              f"{self.strength * 2}")
        
    def shout_taunt(self, tauntee):
        """Express a merciless taung that weakens the tauntee"""
        print(f"\n{self.name} says \"{self.taunt}\"")
        taunt_power = random.randint(1,5)
        tauntee.strength -= taunt_power
        print(f"{tauntee.name} is shaken. Their strength lowers by {taunt_power}\n"
              f"{tauntee.name}'s strength is now {tauntee.strength}")   
        
 
# create a new instance of the Character class and store it in frodo       
frodo = Character("Frodo Baggins", "Hobbit", 10, "Butter Knife",
                  "At least I don't have to carry you AND the ring!")
legolas = Character("Legolas", "Elf", 25, "Bow and Arrow",
                    "That's a nice try... if you were fighting the air!")


# Modify attributes dynamically
frodo.strength += 5
print(f"\nAfter having 2nd breakfast, {frodo.name}'s strength "
      f"is now {frodo.strength}.")


frodo.shout_taunt(legolas)
legolas.shout_taunt(frodo)

bilbo = "why hello"

print(frodo)
print(legolas)
print(frodo.taunt)
print(legolas.weapon)

print(isinstance(frodo, Character))
print(isinstance(legolas, Character))
print(isinstance(bilbo, str))

frodo.attack()
legolas.attack()

