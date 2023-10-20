import random

secret_number = random.randint(1, 100)  

for _ in range(100):
    user_guess = int(input("Guess a number between 1 and 100: ")) 
    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number.") 
        break  
    elif user_guess < secret_number: 
        print("Too low! Try again.") 
    else: 
        print("Too high! Try again.")  
else:
    print(f"You didn't guess the correct number. The correct number was {secret_number}.")