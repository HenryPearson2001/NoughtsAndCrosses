5# a game of noughts and crosses with recursively built AI

from time import time

# prints out the board in a readable way
def printBoard(board):
    for i in range(0,3):
        print(board[i])

# returns empty spaces in the board
def checkSpaces(board):
    emptyLocations = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == " ":
                emptyLocations.append([i,j])
    return emptyLocations

# returns 1 for a win, 0 for a draw and 2 for undetermined
def getResults(board, playerSymbol):
    # if a game can be decided yet
    if len(checkSpaces(board)) <= 4:
        # check rows
        for i in range(0,3):
            if board[i][0] ==  board[i][1] and  board[i][1] ==  board[i][2] and  board[i][0] != " ":
                return 1
        # check columns
        for j in range(0,3):
            if board[0][j] ==  board[1][j] and  board[1][j] ==  board[2][j] and  board[0][j] != " ":
                return 1
        # check diagonals
        if board[0][0] ==  board[1][1] and  board[1][1] ==  board[2][2] and  board[0][0] != " ":
                return 1
        if board[0][2] ==  board[1][1] and  board[1][1] ==  board[2][0] and  board[0][2] != " ":
                return 1
    # check for a draw
    
    if len(checkSpaces(board)) == 0 and board[0][0] != " ":
        return 0
    # otherwise say undecided
    return 2

# calculates the best possible move for symbol
def getMax(board,symbol):
    bestScore = -2
    # work out the available moves
    moves = checkSpaces(board)
    count = 0
    # keep searching until found a move guaranteed to win or all moves explored
    while bestScore < 1 and count < len(moves):
        # work out the current game state
        newBoard = board
        newBoard[moves[count][0]][moves[count][1]] = symbol
        # calculate the score for the current game state
        result = getResults(board,symbol)
        # if the game is not ended by that move (does not result in a win, draw or a loss), work out the best move
        if result == 2:
            # swap the symbols
            if symbol == "X":
                newSymbol = "O"
            else:
                newSymbol = "X"
            # takes the best move the opponent from this position and uses that score to rank their move
            minimum = getMin(newBoard,newSymbol)
            if minimum[1] > bestScore:
                bestMove = moves[count]
                bestScore = minimum[1]
        # if move does decide the game, check if that is better than the current best possible move
        else:
            if result > bestScore:
                bestMove = moves[count]
                bestScore = result
        # reset the baord
        newBoard[moves[count][0]][moves[count][1]] = " "
        count += 1
    return [bestMove,bestScore]

# calculates the worst possible for the ai originally calling this function
def getMin(board,symbol):
    worstScore = 2
    # work out the available moves
    moves = checkSpaces(board)
    count = 0
    # keep searching until found a move guaranteed to lose or all moves explored
    while worstScore > -1 and count < len(moves):
        # work out the current game state
        newBoard = board
        newBoard[moves[count][0]][moves[count][1]] = symbol
        # calculate the score for the current game state
        result = getResults(board,symbol)
        # if the game is not ended by that move (does not result in a win, draw or a loss), work out the best move
        if result == 2:
            # swap the symbols
            if symbol == "X":
                newSymbol = "O"
            else:
                newSymbol = "X"
            # takes the best move the opponent from this position and uses that score to rank their move
            maximum = getMax(newBoard,newSymbol)
            if maximum[1] < worstScore:
                worstMove = moves[count]
                worstScore = maximum[1]
         # if move does decide the game, check if that is better than the current worst possible move
        else:
            if -result < worstScore:
                worstMove = moves[count]
                worstScore = -result
        # reset the board
        newBoard[moves[count][0]][moves[count][1]] = " "
        count += 1
    return [worstMove,worstScore]
    
# main function to play game
def main():
    # create the empty board
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    # allow to human player to pick a symbol and ask whether they want to go first
    humanPlayerSymbol = input("Pick a symbol (X/O):\n")
    # validates input
    while humanPlayerSymbol != "X" and humanPlayerSymbol != "O":
        humanPlayerSymbol = input("Pick a SPECIFIED symbol (X/O):\n")
    if input("Do you want to go first? (y/n) \n") == "y":
        currentPlayerSymbol = humanPlayerSymbol
    else:
        if humanPlayerSymbol == "X":
            currentPlayerSymbol = "O"
        else:
            currentPlayerSymbol = "X"
    # while neither player has won or lost you keep playing
    while getResults(board,currentPlayerSymbol) == 2:
        printBoard(board)
        # if its the human players turn - take input, validate input and then update the board
        if currentPlayerSymbol == humanPlayerSymbol:
            spaces = checkSpaces(board)
            move = input("Please enter the coordinates of your move (x,y):\n")
            while [int(move[1]) - 1,int(move[0]) - 1] not in spaces:
                move = input("Please select an available space (x,y):\n")
            board[int(move[1]) - 1][int(move[0]) - 1] = currentPlayerSymbol
        else:
            # for computers turn, use getNextMove function to get best move, and then update the board
            print("The computers turn: \n")
            mutableBoard = board
            startTime = time()
            move = getMax(mutableBoard,currentPlayerSymbol)
            endTime = time()
            print("time taken:\n",endTime-startTime)
            board[move[0][0]][move[0][1]] = currentPlayerSymbol
        # switch current player's turn
        if currentPlayerSymbol == "X":
            currentPlayerSymbol = "O"
        else:
            currentPlayerSymbol = "X"
    # when an outcome has been reached, output result
    printBoard(board)
    result = getResults(board,currentPlayerSymbol)
    if result == 1 and currentPlayerSymbol == "X":
        print("O won this game :). Nice")
    elif result == 1 and currentPlayerSymbol == "O":
        print("X won this game :). Nice")
    else:
        print("T'was a draw")



main()







                     
