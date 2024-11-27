# Base class representing all beings in Middle-earth
class MiddleEarthBeing:
    def __init__(self, name, race):
        self.name = name  # Public attribute
        # encapsulation - protecting things inside a class
        self._race = race  # Protected attribute - signals not to use outside class
        self.__secret_ability = "Unknown"  # Private attribute

    def reveal_identity(self):
        """Abstraction: A method to be overridden in subclasses"""
        return f"My name is {self.name}, and I am a {self._race}."
    
    # Getters and Setters
    # Provide a controlled way to access and modify an object's attributes. 
    # They ensure proper encapsulation, allowing you to:
    # --Validate input when setting an attribute (e.g., prevent invalid values).
    # --Format or compute values dynamically when retrieving an attribute.
    # --Can change attributes values in other classes
    # --Future-proof code - change how the getter or setter works, not the code outside of the class    

    def get_secret_ability(self):
        """Getter - Provide controlled access to a private attribute"""
        return f"{self.name}'s secret ability is {self.__secret_ability}."
    
    def set_secret_ability(self, secret_ability):
        """Setter - Provide controlled access to change a private attribute"""
        self.__secret_ability = secret_ability
        return f"{self.name}'s secret ability is now {self.__secret_ability}."
    

print(f"{"-" * 15}MiddleEarthBeing Class{"-" * 15}")
some_dwarf = MiddleEarthBeing("Unknown", "Dwarf")
print(some_dwarf.name)
print(some_dwarf._race) # protected attributes can but SHOULD NOT be accessed outside class
print(some_dwarf.reveal_identity())
#print(some_dwarf.__secret_ability) # can't do this, __secret_ability is private
print(some_dwarf.get_secret_ability())
print(some_dwarf.set_secret_ability("Collecting Gold"))

# This class inherits from MiddleEarthBeing - Elf has what MiddleEarthBeing has
class Elf(MiddleEarthBeing):
    def __init__(self, name, race, weapon, secret_ability="Elven Agility"):
        super().__init__(name, race)  # Call the parent class constructor (MiddleEarthBeing)
        self.weapon = weapon  # Unique to Elf
        # can use the setter to override Elf's inherited secret_ability
        self.set_secret_ability(secret_ability)

    def reveal_identity(self):
        """Method overriding - Polymorphism"""
        return f"I am {self.name}, an {self._race} who wields a {self.weapon} with grace."

    def attack(self):
        """Specific method for Elves"""
        return f"{self.name} attacks swiftly with their {self.weapon}."
    
print(f"\n{"-" * 15}Elf Class{"-" * 15}")
legolas = Elf("Legolas", "Elf", "Bow and Arrow")
print(legolas.name)
print(legolas.weapon)
print(legolas.reveal_identity())
print(some_dwarf.reveal_identity())

# DarkElf now inherits from Elf which inherits from MiddleEarthBeing
class DarkElf(Elf):
    def __init__(self, name, race, spell, weapon, secret_ability="Necromancy"):
        super().__init__(name, race, weapon) 
        self.spell = spell
        self.set_secret_ability(secret_ability)
        
    def get_secret_ability(self):
        """Polymorphism: Overrides getter from MiddleEarthBeing 
           Uses super() to get the ability
        """
        return super().get_secret_ability()

    def reveal_identity(self):
        """Polymorphism: Overrides both parent classes"""
        return (f"I am {self.name}, a {self._race} skilled in {self.get_secret_ability()} " 
                f"I wield a {self.weapon} and am able to cast {self.spell}.")
        
    def cast_spell(self):
        """Only Dark Elves can do this"""
        return f"{self.name} casts {self.spell}."
    
    
print(f"\n{"-" * 15}Dark Elf Class{"-" * 15}")
maeglin = DarkElf("Maeglin", "Dark Elf", "Raise Dead", "Short Sword")
print(maeglin.name)
print(maeglin.weapon)
print(maeglin.spell)
print(maeglin.reveal_identity())
print(maeglin.attack())
print(maeglin.cast_spell())
#print(legolas.cast_spell())
print(maeglin.get_secret_ability())