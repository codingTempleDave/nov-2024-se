def duel_sith(sith):
    """
    Simulates a duel with a Sith, handles input errors, and calculates the outcome.
    
    Parameter:
    sith (str): the Sith being dueled
    
    Returns:
    None
    """
    try:
        # Validate that the Sith's name is a string; raise an error otherwise
        if not isinstance(sith, str):
            raise TypeError("Sith's name must be a string!")
        
        # Prompt the user to input their Jedi rank, which will affect the outcome
        force_rank = int(input("Enter your Jedi Rank " 
                               "(0 - Youngling | 1 - Jedi Knight | 2 - Padawan): "))
        
        # Perform a calculation that could potentially raise a ZeroDivisionError
        result = 100 / force_rank
        
    except ZeroDivisionError:
        # This occurs if the user inputs 0 for their Jedi rank
        print("Younglings are wimpy, you were defeated. 💀")
    except ValueError:
        # This handles cases where the input is not a valid integer
        print("Invalid stamina input! Please enter a number.")
    except TypeError as e:
        # This catches the error raised if the Sith's name is not a string
        print(e)
    else:
        # This block executes only if no exceptions occur in the try block
        print(f"You defeated {sith} with {result:.2f}% of your strength remaining!")
    finally:
        # The code in this block always executes, regardless of exceptions
        print("Thanks for playing!")

# Main menu loop
user_choice = 0
while user_choice != 2:  # Loop until the user chooses to exit
    print("\nMain Menu")
    print("1. Duel a Sith")
    print("2. Exit")

    try:
        # Prompt the user to choose an option and ensure it is a valid integer
        user_choice = int(input("Please choose an option (1 or 2): "))

        if user_choice == 1:
            try:
                # Ask the user for the Sith opponent's name
                sith_to_duel = input("Enter your opponent: ")
                
                # Check if the name is empty and raise an error if so
                if not sith_to_duel.strip():
                    raise ValueError("Sith name cannot be empty!")
                
                # Proceed to duel the Sith
                duel_sith(sith_to_duel)
            
            except ValueError as e:
                # Catch and display errors related to the Sith name
                print(e)
        
        elif user_choice == 2:
            # Exit the game with a goodbye message
            print("Goodbye! May the force be with you!")
        
        else:
            # Notify the user if they enter an invalid menu option
            print("Invalid option. Please choose 1 or 2.")

    except ValueError:
        # Catch non-integer input when selecting a menu option
        print("Please enter a valid number.")
