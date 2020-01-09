import random

def drawBoard(board): #This function will print out the board 
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter(): #this lets the player type in the letter they want to be 
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper() # this saves the input and the .upper return a copt of a sting uppercase.
    
    if letter == 'X': #this set the first letter as the player and the second as the computers.
        return ['X', 'O']
    else:
        return['O', 'X']

def whoGoesFirst(): #this choose whos goes first randomaly 
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'

def makeMove(board, letter, move):
    board[move] = letter 

def isWinner(bo, le):# Given a board and a player's letter, this function returns True if that player has won.We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.     
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side 
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board): #this makes a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move): # this will Return True if the passed move is free on the passed board.
    return board [move] == ' '

def getPlayerMove(board):# Let the player enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList): #this will return a valid move from the passed list on the passed board and retun none if there is no valid move.
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter): #Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10): # Here is our algorithm for our Tic Tac Toe AI and First check if we can win in the next move
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10): # Check if the player could win on his next move, and block them.
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) # Try to take one of the corners, if they are free.
    if move != None:
        return move

    if isSpaceFree(board, 5): # Try to take the center, if it is free.
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8]) # Move on one of the sides.

def isBoardFull(board):# this will return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic-Tac-Toe!!')

while True: # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player': # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)# Computer's turn.
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break