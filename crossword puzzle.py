board = [[" ", " ", " ", "*", " ", " ", " "],
         [" ", " ", " ", "*", " ", " ", " "],
         [" ", " ", " ", "*", " ", " ", " "],
         ["*", "*", "*", "*", "*", "*", "*"],
         [" ", " ", " ", "*", " ", " ", " "],
         [" ", " ", " ", "*", " ", " ", " "],
         [" ", " ", " ", "*", " ", " ", " "],
         ]


def print_board(board):
    for row in board:
        print(" ".join(row))


def play_crossword(board):
    print_board(board)
    while True:
        row = int(input("Enter the row (0-6): "))
        col = int(input("Enter the column (0-6): "))
        if row < 0 or row > 6 or col < 0 or col > 6:
            print("Invalid move. Try again.")
            continue
        if board[row][col] == "*":
            print("You lost!")
            break
        board[row][col] = "X"
        print_board(board)


play_crossword(board)
