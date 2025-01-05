import random

print("Weclome to a random dice")
print("Help you with your decision \n\n")


class Game:
    while True:
        dice = ["1","2","3","4","5","6"]
        dice = random.choice(dice)
        dice = random.choice(dice)
        
        Choice = input("Press r to roll dice press q to end: ")
        if Choice == "r":
            print(dice)
        elif Choice == "q":
            exit()