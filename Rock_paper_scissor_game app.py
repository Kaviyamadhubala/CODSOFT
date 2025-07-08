import random
print("Rock Paper Scissors Game")
user=input("Choose rock,paper or scissors:").lower()
options=["rock","paper","scissor"]
computer=random.choice(options)
print("You chose:",user)
print("Computer chose:",computer)
if user==computer:
    print("It's a tie!")
elif (user=="rock" and computer=="scissors")or(user=="paper" and computer=="rock")or(user=="paper" and computer=="paper"):
    print("You win!")
elif user in options:
    print("computer wins!")
else:
    print("Invalid input!")
