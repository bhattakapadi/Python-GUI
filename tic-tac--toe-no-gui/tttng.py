from logik import * 
from input import *


def changePlayer(player):

    if player == 'X':
        newPlayer ='O'
    else:
        newPlayer = "X"
    return newPlayer


if __name__ == "__main__":
    init()
    
    player = "X"

    
    while getGameStatus() == 'RUNNING': #logik.gameStatus
        printGame()
        print(f"Enter the input  {player}: ")
        inputX,inputY = getInput()
        applyInput(inputX,inputY,player)
        checkGameStatus(player)
        player =changePlayer(player)

    

    if getGameStatus() == 'DRAW':
        print(f"The Game is a draw")
    else:
        print(f"{changePlayer(player)} has won")
