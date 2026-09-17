# Dice Rolling Game

# # ASK : ROLL THE DICE?
#IF USER ENTERS Y
#GENERATE TWO RANDOM NUMBERS
#PRINT THEM
#IF USER ENTERS N
#PRINT THANK YOU MESSAGE
#TERMINATE
#ELSE
#PRINT INVALID CHOICE
'''import random
while True:
       choice=input("Roll the dice? (y/n):").lower()
       if choice=='y':
            die1=random.randint(1,6)
            die2=random.randint(1,6)
            print(f'({die1},{die2})')
       elif choice=='n':
            print("Thanks for playing")
            break
       else:
             print("Invalid choice!")'''



# Number Guessing Game

#ASK THE USER TO MAKE A GUESS
#IF NOT A VALID NUMBER
#PRINT AN ERROR
# IF NUMBER < GUESS
# PRINT TOO LOW
#IF NUMBER > GUESS 
# PRINT TOO HIGH
#ELSE
#PRINT WELL DONE
 
'''import random
number_to_guess=random.randint(1,100)
while True:
    try:
        guess=int(input("Guess the number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif(guess > number_to_guess):
            print("Too high!")
        else:
            print("Congratulation! You guessed")
            break
    except ValueError:
        print("Please enter a valid number")'''

# Rock, Paper, Scissors Game

#ASK THE USER TO MAKE A CHOICE
#IF CHOICE IS NOT VALID
#PRINT AN ERROR
# LET THE COMPUTER TO MAKE A CHOICE
# PRINT CHOICE (EMOJIS)
#DETERMINE THE WINNER
#ASK THE USER IF THEY WANT TO CONTINUE
#IF NOT
# TERMINATE

'''import random

emojis = {'r': '🪨', 's': '✂️', 'p': '📄'}
choices = ('r', 's', 'p')

while True:
    user_choice = input("Rock paper or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print('Invalid choice')
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        print("You win")
    else:
        print("You lose")

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break'''

import torch

print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

                
     


