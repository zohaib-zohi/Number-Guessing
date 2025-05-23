import random

computer_guess = random.randint(1, 100)
# print(computer_guess)

user_guess = None
guesses = 0


while user_guess != computer_guess:
    user_guess = int(input("Enter any random number in between 1--100: "))
    guesses += 1
    if user_guess == computer_guess:
        print("You Entered Correct Number !")
    else:
        if user_guess > computer_guess:
            print("You Entered Wrong Number, Enter Smaller Number !")
        else:
            print("You Entered Wrong Number, Enter Larger Number !")

print(f"Congrats you done it in {guesses} guesses")

with open("High_score.txt", "r") as f:
    High_score = int(f.read())

if guesses < High_score:
    print("*** You broke the Highscore hurrah! ***")
    with open("High_score.txt", "w") as f:
        f.write(str(guesses))
