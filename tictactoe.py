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
    insertpiece(board, location, 'X')

def minimax(maximizing : bool, depth, board):
    symbol = 'O' if maximizing else 'X'
    print(f'Symbol is {symbol}')
    print(f'Searching... Depth: {depth}')
    time.sleep(2)
    newstate=board.copy()
    for i in [8,7,6,5,4,3,2,1]:
        if newstate[i]==' ':
            insertpiece(newstate, i, 'O')


def computermove(board):
    for i in [8,7,6,5,4,3,2,1,0]:
        if board[i]==' ':
            insertpiece(board, i, 'O')
            break
        else:
            continue

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
            while len(countempty(board)) > 0 and goes_first == 'n':
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
                else:
                    continue
        elif goes_first=='y':
            while len(countempty(board)) > 0 and goes_first == 'y':
                playermove(board)            
                if windetected('X', board):
                    printboard(board)
                    print('You win!')
                    time.sleep(5)
                    goes_first=' '
                    break
                computermove(board)
                printboard(board)
                if windetected('O', board): 
                    print('Computer wins!')
                    time.sleep(5)
                    goes_first=' '
                    break
                else:
                    continue
        else:
            clean()
            sys.exit()

if __name__ == '__main__':
    main()
