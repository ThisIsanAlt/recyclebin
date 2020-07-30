import sys
import time
import platform
from os import system
import math

def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')

def printboard(board):
    print(f'''|{board[0]}|{board[1]}|{board[2]}|
|{board[3]}|{board[4]}|{board[5]}|
|{board[6]}|{board[7]}|{board[8]}|''')

def countempty(board):
    emptylist = []
    for i in board:
        if i == ' ':
            emptylist.append(i)
    return emptylist

def insertpiece(board, location, symbol):
    board[location]=symbol
    return board

def playermove(board):
    location = int(input('Where do you want to place your symbol?'))-1
    while board[location] != ' ':
        print('That\'s not a valid move! Please try again!')
        location = int(input('Where do you want to place your symbol?'))-1
    insertpiece(board, location, 'X')


def minimax(board, depth, initial, maximizing: bool):
    if windetected('X', board):
        return -depth
    elif windetected('O', board):
        return depth
    #9 is the deepest depth, as depth gets deeper, depth number increases
    elif depth == 9:
        return 0

    maximizing = False if maximizing else True
    
    #initalize your variables
    idealMove = 0
    #initalize your maxEval to very small value
    maxEval = -100000000000000000000000
    #inital yr minEval to very small value
    minEval = 100000000000000000000


    if maximizing:
        #loop through each possible state so we can eval them
        for cell in range(0,8):
            newState = board.copy()
            insertpiece(board, cell, 'O')
            eval = minimax(newState, depth+1, initial, maximizing)
            
            #if we are at inital depth and the current eval is greater than the previous max Eval, then set idealPath to this move
            if depth == initial and eval > maxEval:
                idealMove = cell
            #if currentEval is greater than the previous Best max eval, then make that max eval
            maxEval = max(maxEval,eval)

            return maxEval



    else:
        for cell in range(0, 8):
            newState = board.copy()
            insertpiece(board, cell, 'X')
            eval = minimax(newState, initial, depth+1, maximizing)
            #if currentEval is greater than the previous Best Min eval. then make that min eval
            minEval = min(minEval, eval)
        
        if depth == initial:
            return idealMove
        else:
            return minEval

def computermove(board):
    insertpiece(board, minimax(board, len(countempty(board)), len(countempty(board)), False), 'O')

def windetected(symbol, board):
    if board[0] == board[1] and board[1] == board[2] and board[0] == symbol: return True
    elif board[3] == board[4] and board[4] == board[5] and board[3] == symbol: return True
    elif board[6] == board[7] and board[7] == board[8] and board[6] == symbol: return True
    elif board[0] == board[4] and board[4] == board[8] and board[0] == symbol: return True
    elif board[2] == board[4] and board[4] == board[6] and board[2] == symbol: return True
    elif board[0] == board[3] and board[3] == board[6] and board[0] == symbol: return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] == symbol: return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] == symbol: return True
    else: return False

def main():
    while True:
        clean()
        print('Use your number pad to move like this:')
        printboard(['01','02','03','04','05','06','07','08','09'])
        print('To quit, just leave the input field empty when the program asks you who will go first.')
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        goes_first=input('Would you like to go first? y/n ').lower()
        if goes_first=='n':
            while goes_first == 'n':
                computermove(board)
                printboard(board)
                if windetected('O', board):
                    print('Computer wins!')
                    time.sleep(5)
                    goes_first=' '
                    break
                playermove(board)
                if windetected('X', board): 
                    printboard(board)
                    print('You win!')
                    time.sleep(5)
                    goes_first=' '
                    break
                elif len(countempty(board))==0:
                    print('It\'s a draw!')
                else:
                    continue
        elif goes_first=='y':
            while goes_first == 'y':
                playermove(board)
                print('player has moved.')
                if windetected('X', board):
                    printboard(board)
                    print('You win!')
                    time.sleep(5)
                    goes_first=' '
                    break
                computermove(board)
                print('computer has moved.')
                printboard(board)
                if windetected('O', board): 
                    print('Computer wins!')
                    time.sleep(5)
                    goes_first=' '
                    break
                elif len(countempty(board))==0:
                    print('It\'s a draw!')
                else:
                    continue
        else:
            clean()
            sys.exit()

if __name__ == '__main__':
    main()
