
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
    if board[location] == ' ':
        insertpiece(board, location, 'X')
    else:
        playermove(board)
    printboard(board)

def computermove(board):
    for i in [8,7,6,5,4,3,2,1,0]:
        if board[i] == ' ':
            insertpiece(board, i, 'O')
            break
    printboard(board)

def main():
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    goes_first=input('Would you like to go first? y/n').lower()
    if goes_first=='n':
        while len(countempty(board)) > 0:
            computermove(board)
            playermove(board)
        main()
    elif goes_first=='y':
        while len(countempty(board)) > 0:
            playermove(board)
            computermove(board)
        main()
    else:
        pass

main()
