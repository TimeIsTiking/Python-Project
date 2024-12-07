import random
Robot = ["rock", "paper", "scissor"]
Robot = random.choice(Robot)
Player = input().lower()
print(Robot)
def main():
    if Robot == "rock":
        if Player == "rock":
            print("Tie")
        elif Player == "paper":
            print("Loss")
        else:
            print("Win")
    elif Robot == "paper":
        if Player == "paper":
            print("Tie")
        elif Player == "scissor":
            print("Loss")
        else:
            print("Win")
    elif Robot == "scissor":
        if Player == "scissor":
            print("Tie")
        elif Player == "paper":
            print("Loss")
        else:
            print("Win")
main()