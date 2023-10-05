from enum import Enum





ROWS = 3
COLUMN = 3

gameArray=[] #game array


class GameStatusClass():
	RUNNING = "RUNNING"
	WON = "WON"
	DRAW = "DRAW"

gameStatus=""


def setGameStatus(status):
	global gameStatus 
	gameStatus=status

def getGameStatus():
	return gameStatus

def getGameArray():
	return gameArray

def setGameArray(array):
	global gameArray 
	gameArray = array


def init():
	game = getGameArray()
	string1=" "
	game = [string1*COLUMN]*ROWS
	setGameArray(game)
	setGameStatus(GameStatusClass.RUNNING)

def applyInput(x,y,player):
	game = getGameArray()
	str1 = game[x]
	list1 = list(str1)
	list1[y] = player
	game[x] = ''.join(list1)
	setGameStatus(game)	


def printGame():

	game = getGameArray()
	print("   1    2    3")
	for row in range(ROWS):
		print(row + 1, end=' ')  # Print row number
		for col in range(COLUMN):
			print(f"| {game[row][col]} ", end='')
		print("|")
		if row < ROWS - 1:
			print("  ---  ---  ---")

def checkGameStatus(currentPlayer):
	gameArray=getGameArray()
	if (
	    (gameArray[0][0] == currentPlayer and gameArray[1][1] == currentPlayer and gameArray[2][2] == currentPlayer) or
	    (gameArray[2][0] == currentPlayer and gameArray[1][1] == currentPlayer and gameArray[0][2] == currentPlayer) or
	    (gameArray[0][0] == currentPlayer and gameArray[0][1] == currentPlayer and gameArray[0][2] == currentPlayer) or
	    (gameArray[1][0] == currentPlayer and gameArray[1][1] == currentPlayer and gameArray[1][2] == currentPlayer) or
	    (gameArray[2][0] == currentPlayer and gameArray[2][1] == currentPlayer and gameArray[2][2] == currentPlayer) or
	    (gameArray[0][0] == currentPlayer and gameArray[1][0] == currentPlayer and gameArray[2][0] == currentPlayer) or
	    (gameArray[0][1] == currentPlayer and gameArray[1][1] == currentPlayer and gameArray[2][1] == currentPlayer) or
	    (gameArray[0][2] == currentPlayer and gameArray[1][2] == currentPlayer and gameArray[2][2] == currentPlayer)
	):
	    setGameStatus(GameStatusClass.WON)

	else:
		empty_space_found = False

		for row in gameArray:
		    for element in row:
		        if element == " ":
		            empty_space_found = True
		            break

		if not empty_space_found:
		    setGameStatus(GameStatusClass.DRAW)
		else:
		    setGameStatus(GameStatusClass.RUNNING)
