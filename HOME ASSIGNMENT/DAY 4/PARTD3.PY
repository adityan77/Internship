# Take input from both players
player1 = input("Player 1, enter Rock, Paper, or Scissors: ")
player2 = input("Player 2, enter Rock, Paper, or Scissors: ")
# Compare the inputs and determine the result
if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins!")
elif (player2 == "rock" and player1 == "scissors") or (player2 == "scissors" and player1 == "paper") or (player2 == "paper" and player1 == "rock"):
    print("Player 2 wins!")
elif player1==player2:
    print("It's A Tie")
else:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")