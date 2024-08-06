import random
userDict = {
    "r": 1,
    "p": 0,
    "s":-1 
}
choiceDict = {
    1: "Rock",
    0: "Paper",
   -1: "Scizzer"
}
user = input("Enter choice: ")
while not(user in ["r","p","s"]):
    user = input("Enter choice again: ")

user_choice =userDict[user]
computer_choice = random.choice([-1, 0, 1])
print(f"\nUsers Choice = {choiceDict[user_choice]}\nComputer Choice = {choiceDict[computer_choice]}")
if(user_choice == computer_choice):
    print("Draw")
else:
    if(computer_choice == 1 and user_choice == 0):
        print("You Win")
    elif(computer_choice == 1 and user_choice == -1):
        print("Computer Win")
    elif(computer_choice == 0 and user_choice == 1):
        print("Computer Win")
    elif(computer_choice == 0 and user_choice == -1):
        print("You Win")
    elif(computer_choice == -1 and user_choice == 0):
        print("Computer Win")
    elif(computer_choice == -1 and user_choice == 1):
        print("You Win")