# The objective is to write a four in a line game. For starters, ignore that the red and blue tokens
# aren't placed at the bottom when entering positions. When you complete the task, as a bonus fix the
# game so that the token is placed at the bottom, example for 3x3 game:
# Red user enters 0, 0, first implementation of game returns (task T1):
#
# R ? ?
# ? ? ?
# ? ? ?
#
# Fixed implementation of game should print out the following: (task T2)
#
# ? ? ?
# ? ? ?
# R ? ?
#
# Also in both implementations, ignore the stacking of tokens, e.g. it is a perfectly valid move to do
# the following:
#
# Red player enters 2 0 on the following field:
#
# R ? ?
# ? ? ?
# ? ? ?
#
# The field then becomes:
#
# R ? ?
# ? ? ?
# R ? ?
#
# As a bonus, when you finish T1 and T2, you can also implement if a move is valid e.g. the token
# can not be put above an empty line (task T3).
#
# BONUS task T4:
# Create a n in a row game, where the player specifies how many tokens must be put in a line or
# diagonally. Make sure that the playfield size is greater or equal to the parameter the user
# passes for n in a row.

def printPlayField(playField):
    for i in range(0, len(playField)):
        for j in range(0, len(playField)):
            if playField[i][j] == 'R':
                print('R ', end = '')
            elif playField[i][j] == 'B':
                print('B ', end = '')
            else:
                print('? ', end = '')
        print()


def checkIfFourInARow(playField, player):
    # TODO: Implement this method. Check if the the player has scored four in a row, you
    # must also check diagonal positions.
    # R B B B
    # ? R B B
    # ? ? R B
    # ? ? ? R
    #
    # Or:
    # R ? B B
    # R ? ? B
    # R ? ? B
    # R ? ? B

    check = False

    if player == 'Red':
        check = 'R'
    else:
        check = 'B'

    for i in range(0, len(playField)):
        tokenCount = 0
        for j in range(0, len(playField)):
            if playField[i][j] == check:
                tokenCount = tokenCount + 1
            else:
                tokenCount = 0
        if tokenCount == 4:
            return True

    tokenCount = 0

    for i in range(len(playField) - 3):
        for j in range(3, len(playField)):
            if playField[i][j] == check and playField[i + 1][j - 1] == check and playField[i + 2][j - 2] == check and \
                    playField[i + 3][j - 3] == check:
                return True

    for i in range(0, len(playField) - 3):
        for j in range(len(playField) - 3):
            if playField[i][j] == check and playField[i + 1][j + 1] == check and playField[i + 2][j + 2] == check and \
                    playField[i + 3][j + 3] == check:
                return True

    return False


def checkIfGameFinished(playField):
    # TODO: Check if game is finished, e.g. no player won and all the fields are set to
    # tokens, for example:
    # R R R B
    # B B R B
    # B B B B
    # R R R R

    count = 0
    for i in range(0, len(playField)):
        for j in range(0, len(playField)):
            if playField[i][j]:
                count = count + 1

    if count == len(playField) * len(playField):
        return True

    return False


def generatePlayField(size):
    playField = []
    for i in range(0, size):
        playField.append([False] * size)
    return playField


def main():
    gameSize = int(input("Enter game field size >= 4: "))
    # TODO: Check if gameSize is even a number ...
    playField = generatePlayField(gameSize)
    playerInTurn = 'Red'
    printPlayField(playField)

    print('To play game, enter positions to place your tokens in e.g. (0 0) or (1 0). Enter q to quit.')

    gameRunning = True
    while gameRunning:
        validMove = False
        gameFinished = checkIfGameFinished(playField)
        if gameFinished:
            print('Nobody won.')
            return
        while not validMove:
            message = playerInTurn + ' player, please enter position:'
            pos = input(message)
            if pos == "q":
                return
            pos = pos.split(' ')
            # TODO: Check user input
            # - Size of pos == 2
            # - First and second element a number
            # - First and second element >= 0 < size
            x = int(pos[0])
            y = int(pos[1])

            # Check if a token is not there yet ...
            if not playField[x][y]:
                if playerInTurn == 'Red':
                    playField[x][y] = 'R'
                else:
                    playField[x][y] = 'B'
                validMove = True

                fourInARow = checkIfFourInARow(playField, playerInTurn)
                if fourInARow:
                    print('Congratulations to the %s player!' % (playerInTurn))
                    return

                # Switch player ...
                if playerInTurn == 'Red':
                    playerInTurn = 'Blue'
                else:
                    playerInTurn = 'Red'
                printPlayField(playField)
            else:
                print('The position you have chosen is already set. Please try again.')


if __name__ == "__main__":
    main()