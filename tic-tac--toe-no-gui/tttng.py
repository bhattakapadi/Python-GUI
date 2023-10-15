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
        # 0 for human
        # 1 for computer(random)
        # 2 for computer(intro)
        easy = False
        if player == 'X':
            compHuman = 0
        else: 
            if easy == True:
                compHuman = 1
            else:
                print("Hard mode computer input ")
                compHuman = 2
        inputX,inputY = getInput(compHuman,player)
        applyInput(inputX,inputY,player)
        checkGameStatus(player)
        player = changePlayer(player)
        printGame()
        print("End of a loop!!")

    

    if getGameStatus() == 'DRAW':
        print(f"The Game is a draw")
    else:
        print(f"{changePlayer(player)} has won")
