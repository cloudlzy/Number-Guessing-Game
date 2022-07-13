import random

NumInt = random.randrange(1, 9)

countChance=0

print("Print a number between 1 and 9")
print("you have 5 chances")

while countChance < 5:
    guess = int(input("Enter your guess: "))
    countChance = countChance + 1

    if guess < NumInt:
        print("Too low! Guess a number higher than ", guess)
        
    if guess > NumInt:
        print("Too high! Guess a number lower than ", guess)

    if guess == NumInt:
        print("You win!")
        break

    if not countChance < 5:
        print("You lose, The number is ", NumInt)
        