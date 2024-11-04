# Fun number guessing game without a while loop

# Variables
secret_number = 7  # The number the user has to guess
max_attempts = 3  # Maximum number of attempts allowed
is_correct = False  # Boolean to track if the guess is correct

# Introduction
print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 10. Can you guess it?")
print(f"You have {max_attempts} attempts.\n")

# First attempt
guess = int(input("Attempt 1 - Enter your guess (a number between 1 and 10): "))

if guess == secret_number:
    print("Congratulations! You guessed it right on your first try!")
    is_correct = True
elif guess < secret_number:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")

# Second attempt
if not is_correct:
    guess = int(input("Attempt 2 - Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right on your second try!")
        is_correct = True
    elif guess < secret_number:
        print("Too low! One last try!")
    else:
        print("Too high! One last try!")

# Third and final attempt
if not is_correct:
    guess = int(input("Attempt 3 - Enter your final guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right on your last try!")
        is_correct = True
    else:
        print("Sorry, you've used all attempts! The correct number was", secret_number)

# Final message
if is_correct:
    print("You won the game!")
else:
    print("Better luck next time!")
