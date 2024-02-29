def chessboard(n):
    board = ""
    for i in range(n):
        for j in range(n):
            if (j + i) % 2 == 0:
                board += "#"
            else:
                board += " "
        board += "\n"
    return board

print(chessboard(10))