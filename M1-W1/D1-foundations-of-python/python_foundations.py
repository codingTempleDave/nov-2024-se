# imports
import random
import time

# comments!!!!   where you would want take notes!!!

''' 
multiline comments
I'm still in a comment!!!
'''

# loosely typed - python figures out what kind of value it is
welcome_message = "The 💣 will explode in 3 incorrect guesses. Will you survive?"
min_number = 1
max_number = 10
secret_number = random.randint(min_number, max_number)
is_correct = False

print(welcome_message)
print(f"The correct number is between {min_number} and {max_number}")
print("You have three attempts. Good luck \"bwahahah!\" 😈")

# 1st guess
guess = int(input("Go ahead and make your first guess: "))

if guess == secret_number:
    print("You guess it on your first try 👿 Sadly, no 💥 for you")
    is_correct = True
elif guess < secret_number:
    print("Too low! 😈 Try again!")
    print() # empty line
else:
    print("Too high! 😈 Try again!")
    print() # empty line    

# 2nd guess
if not is_correct:
    guess = int(input("You're getting closer to your demise, make your 2nd guess: "))
    
    if guess == secret_number:
        print("Curses you're 2nd guess was correct! 👿 Enjoy your freedom...")
        is_correct = True
    elif guess < secret_number:
        print("Too low! 😈 Try again!")
        print() 
    else:
        print("Too high! 😈 Try again!")
        print() 

# 3rd guess        
if not is_correct:
    guess = int(input("Last chance! Bwahaha!  Enter your final guess: "))
    
    if guess == secret_number:
        print("How did you...? 👿 You have survived for now...")
        is_correct = True
    else:
        print("Incorrect! The number was: ", secret_number)
        print("😈 Your time has come bwahaha!")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("💥💥💥💥💥💥💥")
        time.sleep(1)
        print()

if is_correct:
    print("You must have cheated... enjoy your freedom 🏃‍➡️🚪")
else:
    print("Sheesh that got kinda dark 😇 Better luck next time!")