# Global vars
jedi_name = "Luke Skywalker"
jedi_rank = "Jedi Knight"
force_power = 100

"""
Docstrings - explanations of functions
    1. What the function does
    2. The received parameters and data types
    3. What is returned and the data type
"""

# functions should only do one thing
def greet_all_jedi(): 
    """
    Greets
    """
    print("Hello Jedi")

greet_all_jedi() # calls or invokes the function


def attack(target, weapon="lightsaber"): # target and wepon are parameters
    """
    Perform an attack on a target with a specified weapon.

    Parameters:
    target (str): The target being attacked.
    weapon (str): The weapon being used. Defaults to "lightsaber".
    
    Returns:
    str: The action of the attack.
    """
    jedi_name = "Obi Wan Kenobi" # local variable
    return f"{jedi_name} attacks {target} with a {weapon}"


# take the argument outside
print(attack("Darth Vader")) # "Dark Vader is the argument"
print(attack("Darth Maul", "stomach slice"))
print(f"The global var jedi_name {jedi_name} was not affected")

def add_force_power(*points):
    print(points[0])
    print(points[1])
    """
    Adds points to the Jedi's force power.

    Parameters:
    *points (int): Multiple point values to be added.
        - The * means it can accept however many arguments passed in
        - Values are placed in a tuple (immutable list)
    
    Returns:
    int: The new total points.
    """
    total_power = sum(points)
    global force_power # uses the global force_power var, not a local one
    force_power += total_power
    return force_power

print(f"Jedi's force power after battle: {add_force_power(50, 75, 25, 12, 6)}")
print(f"The global var force_power was changed to {force_power}")


def use_force(power, **kwargs):
    """
    Use the Force to perform an action with additional effects.

    Parameters:
    power (str): The type of Force power.
    **kwargs: Additional named arguments (e.g., 'duration', 'intensity').
        - accepts "key = value" arguments and puts them in a dictionary

    Returns:
    str: Description of the Force action.
    """
    action_details = ""
    
    for key, value in kwargs.items():
        action_details += key + " : "
        action_details += value + " | "        
    
    # another way of doing this using a shorthand method
    #action_details = ' | '.join(f"{key}: {value}" for key, value in kwargs.items())
    
    return f"{jedi_name} uses {power} with the following effects: {action_details}."

print(use_force("Telekinesis", duration="5 seconds", intensity="High"))



missions = ['Training with Yoda', 'Battle with the Empire', 'Learning the Force']

def manipulate_missions(action, *new_missions):
    """
    Manipulates the Jedi's list of missions.

    Parameters:
    action (str): Action to perform on the list ('add', 'remove', 'clear').
    *new_missions (str): New missions to be added or removed.

    Returns:
    list: The updated missions list.
    """
    global missions
    if action == "add":
        missions.extend(new_missions) # adds a list to a current list
        return missions
    elif action == "remove":
        for mission in new_missions:
            if mission in missions:
                missions.remove(mission)
        return missions
    elif action == "clear":
        missions.clear()
        return missions
    else:
        return "Invalid action. Please use 'add', 'remove', or 'clear'."
    
print(f"Current Missions: {missions}")
print(manipulate_missions("add", "Rescue Han Solo", "Infiltrate Death Star"))
print(f"Current Missions: {missions}")
print(manipulate_missions("remove", "Battle with the Empire"))
print(f"Updated Missions: {missions}")