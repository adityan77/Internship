A = input("Enter input for A (Rock,Paper,Scissors) : ")
B = input("Enter input for B (Rock,Paper,Scissors) : ")


if A == B:
    print("It's a tie!")
elif A == "rock":
    if B == "scissors":
        print("A wins!")
    elif B == "paper":
        print("B wins!")
    
elif A == "paper":
    if B == "rock":
        print("A wins!")
    elif B == "scissors":
        print("B wins!")
    
elif A == "scissors":
    if B == "paper":
        print("A wins!")
    elif B == "rock":
        print("B wins!")

