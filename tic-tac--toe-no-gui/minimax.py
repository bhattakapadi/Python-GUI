import math
import copy


def checkGame(gameArray,currentPlayer):
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
		return "WON"

	else:
		empty_space_found = False

		for row in gameArray:
			for element in row:
				if element == " ":
					empty_space_found = True
					break

		if  empty_space_found == False:
			return "DRAW"
		else:
			return "RUNNING"




def make_move(game,move,player):
	#print(f"make_move::game{str(game)}, move: {move}")
	str1 = game[move[0]]
	list1 = list(str1)
	list1[move[1]] = player
	game[move[0]] = ''.join(list1)
	return game


def getPossibleMoves(array):
	moves=[]

	for i in range(0,3):
		for j in range(0,3):
			if array[i][j] == " ":
				moves.append([i,j])

	return moves


def changePlayer(player):

	if player == 'X':
		newPlayer ='O'
	else:
		newPlayer = "X"
	return newPlayer





def getGameState(game,player):
	nextPlayer = changePlayer(player)
	if checkGame(game,player) == "DRAW" or checkGame(game,nextPlayer) == "DRAW":
		return "DRAW"
	elif checkGame(game,player) == "WON" or checkGame(game,nextPlayer) == "WON":
		return "WON"

	return "RUNNING"

def getWinner(game):
	if checkGame(game,"X") == "WON":
		return "X"
	else: 
		return "O"


def minimax(isMaxTurn, maximizerMark, board):
	state = getGameState(board,maximizerMark)
	if state == "DRAW":
		return 0
	elif state == "WON":
		return 10 if getWinner(board) is maximizerMark else -10

	player = maximizerMark if isMaxTurn else changePlayer(maximizerMark)

	scores = []
	moves = getPossibleMoves(board)
	for move in moves:
		tmpArray2 = make_move(copy.deepcopy(board), move, player)
		scores.append(minimax(not isMaxTurn, maximizerMark, tmpArray2))

	return max(scores) if isMaxTurn else min(scores)    


def make_best_move(game, player):
	bestScore = -math.inf
	bestMove = None
	tmpArray2 = copy.deepcopy(game)   # Create a deep copy of the game board
	moves = getPossibleMoves(tmpArray2)


	for move in moves:
		tmpArray2 = make_move(copy.deepcopy(game), move, player)
		score = minimax(False, player, tmpArray2)
		if score > bestScore:
			bestScore = score
			bestMove = move
	return bestMove


def getPosition(game,player):
	cordinate = make_best_move(game,player)
	return cordinate