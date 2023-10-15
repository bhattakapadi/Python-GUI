from logik import *

from minimax import *
import random

ROWS=3
COLUMN=3


#returns true if the input is within the rage
#returns false if the input is out of bound
def outOfBound(x,y):
	if (x < 0 or x > ROWS) or (y < 0 or y > COLUMN):
		return False
	return True


#check if the position is empty
def validPosition(x,y):
	gameBoard = getGameArray()
	if gameBoard[x][y] == " ":
		return True
	return False

def userInput():
	validInput = False

	while validInput == False:
		print("The value of x and y should be between 1 to 3")
		x = int(input("Enter a ROW number (1-3): "))
		y = int(input("Enter a COLUMN number(1-3): "))
		validInput= outOfBound(x,y)
		if validInput == True: 
			validInput = validPosition(x-1,y-1)

	return x-1,y-1


def compRandomInput():
	validInput = False
	while validInput == False:
		print("The value of x and y should be between 1 to 3")
		x = random.randint(1,3)
		y = random.randint(1,3)
		validInput= outOfBound(x,y)
		if validInput == True: 
			validInput = validPosition(x-1,y-1)

	return x-1,y-1



def compHardInput(player):
	print("The value of x and y should be between 1 to 3")
	x,y = getPosition(getGameArray(),player)
	print(f"x: {x} + y: {y}")
	return x,y



def getInput(num,player):
	if num == 0:
		x,y = userInput()
	elif num == 1:
		x,y = compRandomInput()
	else:
		x,y = compHardInput(player)
	return x,y  #array start from 0


