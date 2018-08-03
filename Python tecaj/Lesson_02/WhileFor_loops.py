secret = 42
guess = False
"""
while guess != secret:
    guess = int(input("Guess number:"))

    if guess == secret:
        print("Correct!")
    else:
        print("Wrong!")

guess = False

for number_of_tries in range(5):
    guess = int(input("Guess number:"))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong! Tries left: " +  str(number_of_tries))

number_of_tries = 1

while number_of_tries <= 5:
    guess = int(input("Guess number:"))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong!")
        print("Tries left: " + str(5 - number_of_tries))
        number_of_tries += 1
"""

for i in range(10):
    print(i)
print("-----")
for i in range(5,10):
    print(i)
print("-----")
for i in range(5,10,2):
    print(i)
