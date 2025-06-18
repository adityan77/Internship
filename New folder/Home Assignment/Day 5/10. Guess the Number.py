num = 9

while True:

    guess = int(input("Guess the number: "))
    if num > guess:
        print("Too low")
    elif num < guess:
        print("Too high")
    else:
        print("Correct")
        break

print("Game Over")
