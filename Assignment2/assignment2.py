boardSize = int(input("What Size Game GoPy?"))
temporary = [i for i in range(boardSize*boardSize)]
board = []
a, b = 0, boardSize
counter = 0
while b <= boardSize*boardSize:
    board.append(temporary[a:b])
    a += boardSize
    b += boardSize


def call():
    for i in range(len(board)):
        for z in range(len(board)):
            print(str(board[i][z]).rjust(3, ' '), end="")
            if z == len(board) - 1:
                print()


call()


def main(number, player):
    selection = int(input("Player "+number+" Turn--> "))
    if selection in temporary:
        board[int(selection) // boardSize][selection % boardSize] = player
        global counter
        counter += 1
        temporary[:] = [player if x == selection else x for x in temporary]
        row = [i for i in range(boardSize) for y in range(boardSize) if board[i][y] == player]
        column = [i for i in range(boardSize) for y in range(boardSize) if board[y][i] == player]
        horizontal1 = [i for i in range(boardSize) if board[i][i] == player]
        horizontal2 = [i for i in range(boardSize) if board[i][-i - 1] == player]
        check = [x for x in range(boardSize) if row.count(x) == boardSize or column.count(x) == boardSize]
        call()
        if len(check) > 0:
            print("Winner:"+player)
            return 0
        if len(horizontal1) == boardSize or len(horizontal2) == boardSize:
            print("Winner:"+player)
            return 0
    else:
        if int(selection) >= boardSize * boardSize or int(selection) < 0:
            print("Please enter a valid number")
            call()
        else:
            key = board[int(selection) // boardSize][int(selection) % boardSize]
            if key == player:
                print("You have made this choice before")
                call()
            else:
                print("The other player select this cell before")
                call()


while True:
    if counter != boardSize*boardSize:
        result1 = main("1", "X")
        if result1 == 0:
            break
    if counter != boardSize*boardSize:
        result2 = main("2", "O")
        if result2 == 0:
            break
    else:
        print("No Winner")
        break
# End Of The File
