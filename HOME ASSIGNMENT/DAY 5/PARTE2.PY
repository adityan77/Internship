# 11.	Guess the Number Game
# •	Set a secret number (e.g., 7)
# •	Let the user guess until they get it right
# •	Print "Too high" or "Too low" for wrong guesses
# •	Print "Correct!" when guessed

sc=17
while True:
    num=int(input("Enter A Number To Guess:-"))
    if num==sc:
        print("You Guess The Correct Number")
        break
    elif num<15:
        print("Too Low Let's Try Again")
    elif num>=15 and num<=25:
        print("You Are Too Close Let's Try Again")
    elif num>=50:
        print("Too High Let's Try Again")

