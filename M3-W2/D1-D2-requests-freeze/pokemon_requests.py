# py -m venv venv | python3 -m venv venv - create virtual env
# venv\Scripts\activate | source venv/bin/activate - activate virtual env 
# pip install requests - install requests package
# pip uninstall (package-name) - uninstalls the package
# python --version - displays version of python from within the virtual environment
# python3.8 -m venv venv - creates a virtual environment using Python 3.8
# pip list - See installed packages
# pip freeze > requirements.txt - Saving list of installed packages
# pip install -r requirements.txt - Install packages in requirements.txt 
# deactivate - deactivates virtual environment
# Be careful what you name your py files (DON'T NAME IT THE SAME AS A PACKAGE)

import requests
import json

# Function to fetch data from PokeAPI for a single Pokémon
def fetch_single_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)    
    data = response.json()  # Convert response to Python dictionary
    abilities = data["abilities"]
    
    print(data["forms"][0]["name"])
    print(data["base_experience"])
    print(data["cries"]["legacy"])
    
    print(f"\n{pokemon_name.capitalize()} Abilities:")
    for ability in abilities:
        print(f"Name: {ability["ability"]["name"]}\n"
              f"URL: {ability["ability"]["url"]}\n")
    
    return data

fetch_single_pokemon("pikachu")

# Your challenge:

# --Use the pokeapi to get the names and urls of 5 pokemons (research how to do this)
# --Print out all 5 names into the console
# --Put all the URLs into a list and print that to the console

# If you have time:
# --Convert the API data back into a JSON string (after using .json())
# --Convert it back into a Python objection (dictionary) (don't use .json())

# Function to fetch data for multiple Pokémon
def fetch_multiple_pokemon(limit=10):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)    
    
    data = response.json()  # Convert response to Python dictionary
    
    print("\nList of Pokémon:")
    for pokemon in data["results"]:
        print(pokemon["name"])  # Loop through and print Pokémon names
        
        # Use list comprehension to extract Pokémon URLs
    pokemon_urls = [pokemon["url"] for pokemon in data["results"]]
    print("\nList of Pokémon URLs:")
    print(pokemon_urls)
    
    return data["results"]  # Return the list of Pokémon


# Fetch data for multiple Pokémon
pokemon_list = fetch_multiple_pokemon(limit=5)

# Serialize Python object to JSON-formatted string using .dumps()
serialized = json.dumps(pokemon_list, indent=4)
print("\nConvert a Python Object to a JSON formatted string:")
print(serialized)
#print(serialized[0]["name"])

# Deserialize JSON string back into a Python object using .loads()
deserialized = json.loads(serialized)
print("\nConvert a JSON formatted strong back to Python object:")
print(deserialized)
print(deserialized[0]["name"])