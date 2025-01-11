
#### 2.1 Number Guessing Game

import random

def guess_number():
    secret = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess the number (1-100): "))
        attempts += 1
        
        if guess == secret:
            print(f"You won! It took {attempts} attempts")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

