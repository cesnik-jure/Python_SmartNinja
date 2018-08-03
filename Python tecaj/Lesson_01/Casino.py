import random

def guessing_game(balance_now):
    print("GUESSING GAME")
    print("-----")
    secret = random.randint(1, 10)
    guess = int(input("Make a guess of a number between 1 and 10: "))
    if guess == secret:
        print("You guessed correctly!")
        balance_now += 1
    else:
        print("Unfortunately, your guess was not correct. The correct guess was: " + str(secret))
        balance_now -= 1
    global balance
    balance = balance_now

def replay(balance_now):
    print("Your current balance is: " + str(balance_now))
    play_again = str(input("Want to play again? (Y/N)"))
    if play_again == "Y" or play_again == "y":
        print("You decided to play again.")
    elif play_again == "N" or play_again == "n":
        print("This is not how this works. You play until you're dry.")
    else:
        print("Unexpected error. You broke the game. Please wait for security to beat you up.")
        global beatup
        beatup = True

balance = 5
beatup = False
print("Your current balance is: " + str(balance))

while balance >= 0:
    print("")
    print("------")
    guessing_game(balance)
    if balance == 0:
        break
    replay(balance)
    if beatup == True:
        break

print("Thank you for giving us all your money. And remember, the casino always wins.")
