import random

print("Thank you for playing my number guessing game")
print("Please pick a number\n\n\n")
print("you will only get 20 trys\n")
print("So think smart")


Guess_random = random.randint(1,100)
Win = False
for i in range(20):
    Guess = int(input())
    
    if Guess_random == Guess:
        Win = True
        
    elif 101 < Guess:
        print("You way over the limit")   
             
    elif Guess_random < Guess:
        print("You must go lower")
            
    elif Guess_random > Guess:
        print("You must go Higher")
    
    if Win:
        print("Your the number 1 Winner and my book")
        break